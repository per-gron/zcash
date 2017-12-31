"""Generates a BUILD.bazel file suitable for ZCash given a libgmp source
directory. Run this script in the libgmp source directory. It creates a
BUILD.bazel file there.
"""
import os
import subprocess
import glob
import re
import generator_util

# TODO(per-gron): Configure host

# TODO(per-gron): This is not very nice; it assumes that the package is
# being imported with a given name.
external_dir = "external/libgmp/"

extra_c_flags = [
    "-DHAVE_CONFIG_H",
    "-fPIC",
    "-w",
    "-I$(GENDIR)/%s" % external_dir,
]

libgmp_config_opts = [
    "--enable-cxx",
    "--disable-shared",
]

libraries = [  # Order is significant
    { "name": "cxx", "dir": "cxx", "deps": [] },
    { "name": "rand", "dir": "rand", "deps": [":gmp_core"] },
    { "name": "scanf", "dir": "scanf", "deps": [":gmp_core"] },
    { "name": "printf", "dir": "printf", "deps": [":gmp_core"] },
    { "name": "mpz", "dir": "mpz", "deps": [":gmp_core"] },
    { "name": "mpq", "dir": "mpq", "deps": [] },
    { "name": "mpn", "dir": "mpn", "deps": [":gmp_core"] },
    { "name": "mpf", "dir": "mpf", "deps": [] },
    { "name": "gmp_core", "dir": ".", "deps": [] },
]

subprocess.call(["./configure"] + libgmp_config_opts)

objs = generator_util.extract_variable_from_makefile("$(libgmp_la_OBJECTS) $(libgmp_la_DEPENDENCIES) $(EXTRA_libgmp_la_DEPENDENCIES) $(CXX_OBJECTS)").split()
cflags = generator_util.extract_variable_from_makefile("$(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)").split()
cflags = [flag for flag in cflags if flag != "-I.."]

make_generated_files = [
    'fib_table.h',
    'fac_table.h',
    'mp_bases.h',
    'trialdivtab.h',
    'mpn/perfsqr.h',
    'mpn/jacobitab.h',
    'mpn/mp_bases.c',
    'mpn/fib_table.c',
]

generated_headers = {
    "config.h": generator_util.read_file("config.h"),
    "config.m4": generator_util.read_file("config.m4"),
    "gmp.h": generator_util.read_file("gmp.h"),
}
for file in make_generated_files:
    subprocess.call(["make", file])
    generated_headers[file] = generator_util.read_file(file)

def extract_linked_files():
    links = {}
    for line in generator_util.read_file("config.log").split('\n'):
        match = re.match(r"^config\.status:\d+: linking ([^ ]+) to ([^ ]+)$", line)
        if not match:
            continue
        links[match.group(2)] = match.group(1)
    return links

def process_linked_file(src, target):
    rule = ""
    rule += "genrule(\n"
    rule += "    name = '%s_copy',\n" % target
    rule += "    srcs = ['%s'],\n" % src
    rule += "    outs = ['%s'],\n" % target
    rule += "    cmd = \"cp $(location %s) $@\",\n" % src
    rule += ")\n\n"

    return rule

def process_linked_files():
    linked_files = extract_linked_files()
    res = ""
    for target in linked_files:
        res += process_linked_file(linked_files[target], target)
    return res

def is_asm_obj(file):
    return os.path.isfile(re.sub(r"\.lo$", ".asm", file))

def is_cpp_obj(file):
    return os.path.isfile(re.sub(r"\.lo$", ".cc", file))

def obj_to_src(file):
    if is_asm_obj(file):
        return re.sub(r"\.lo$", ".s", file)
    if is_cpp_obj(file):
        return re.sub(r"\.lo$", ".cc", file)
    else:
        return re.sub(r"\.lo$", ".c", file)

def process_asm_genrules():
    rule = ""

    extra_srcs = [
        'config.m4',
        'mpn/asm-defs.m4',
        'mpn/x86_64/x86_64-defs.m4',
    ]

    asm_srcs = [re.sub(r"\.lo$", ".asm", file) for file in objs if is_asm_obj(file)]
    for asm_src in asm_srcs:
        out = re.sub(r"\.asm$", ".s", asm_src)
        operation = os.path.splitext(os.path.basename(asm_src))[0]
        rule += "genrule(\n"
        rule += "    name = '%s_asm',\n" % asm_src
        rule += "    srcs = ['%s'] + %s + glob(['mpn/x86_64/**/*.asm']),\n" % (asm_src, extra_srcs)
        rule += "    outs = ['%s'],\n" % out
        # Bazel has this thing that generated files reside in a different
        # directory tree than input files. The way m4 is used in libgmp does not
        # agree with that structure. As a workaround, config.m4 (which is a
        # generated file) is copied into the input file tree.
        #
        # The first command here uses cat x > y instead of cp because otherwise
        # the output is read-only (because the input is in this case), which can
        # cause some minor trouble.
        #
        # In the path $$(dirname $(location mpn/asm-defs.m4))/../config.m4
        # the /../ is significant: $$(dirname $(location mpn/asm-defs.m4))
        # points to a symlink and merely taking the dirname of that is not
        # the same as appending /..
        rule += "    cmd = \"cat $(location config.m4) > $$(dirname $(location mpn/asm-defs.m4))/../config.m4 && cat $(location %s) | (cd $$(dirname $(location mpn/asm-defs.m4)) && m4 -DOPERATION_%s) > $@\",\n" % (asm_src, operation)
        rule += ")\n\n"

    return rule

def process_main_library():
    rule = ""
    rule += "cc_library(\n"
    rule += "    name = 'gmp',\n"
    rule += "    visibility = ['//visibility:public'],\n"
    rule += "    hdrs = ['gmp.h', 'gmpxx.h'],\n"
    rule += "    deps = %s,\n" % [lib["name"] for lib in libraries]
    rule += ")\n\n"
    return rule

def process_library(name, descriptor):
    dir = descriptor["dir"]

    def belongs_here(file):
        return (os.path.dirname(file) or ".") == dir

    def src_label(src):
        return "%s_with_operation" % src

    needs_operation = { "mpn": True, "mpz": True }.get(name, False)

    def preprocessed_file(src):
        if needs_operation:
            return os.path.join(
                os.path.dirname(src),
                'pp_' + os.path.basename(src))
        else:
            return src

    srcs = [obj_to_src(file) for file in objs if belongs_here(file)]

    hdrs = "glob(['*.h', '%s/*.h'])" % dir
    if dir == ".":
        hdrs = "glob(['*.h'])"

    rule = ""

    local_c_flags = ["-I%s%s" % (external_dir, dir)]

    if needs_operation:
        for src in srcs:
            # Bazel does not support per-file copts. Hack around by adding a #define
            # to each file.
            operation_cflag = "OPERATION_%s" % os.path.splitext(os.path.basename(src))[0]
            rule += "genrule(\n"
            rule += "    name = '%s',\n" % src_label(src)
            rule += "    srcs = ['%s'],\n" % src
            rule += "    outs = ['%s'],\n" % preprocessed_file(src)
            rule += "    cmd = 'echo \"#define %s 1\" > $@ && cat $(location %s) >> $@'\n" % (operation_cflag, src)
            rule += ")\n\n"

    rule += "cc_library(\n"
    rule += "    name = '%s',\n" % name
    rule += "    copts = %s,\n" % (cflags + extra_c_flags + local_c_flags)
    rule += "    linkstatic = 1,\n"
    rule += "    hdrs = %s,\n" % hdrs
    rule += "    srcs = %s + generated_includes,\n" % [preprocessed_file(src) for src in srcs]
    rule += ")\n\n"

    return rule

def process_libraries():
    res = ""
    for lib in libraries:
        res += process_library(lib["name"], lib)
    return res

def process_generated_headers():
    res = ""
    for generated_header in generated_headers:
        res += generator_util.copy_file_genrule(generated_header, generated_headers[generated_header])
    return res


generated_includes = ['config.h', 'gmp.h', 'gmp-mparam.h'] + [file for file in make_generated_files if file.endswith('.h')]

build_file = generator_util.build_header()
build_file += "generated_includes = %s\n" % generated_includes
build_file += process_main_library()
build_file += process_libraries()
build_file += process_asm_genrules()
build_file += process_linked_files()
build_file += process_generated_headers()

generator_util.write_file("BUILD.bazel", build_file)
