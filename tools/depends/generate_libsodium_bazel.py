"""Generates a BUILD.bazel file suitable for ZCash given a libsodium source
directory. Run this script in the libsodium source directory. It creates a
BUILD.bazel file there.
"""

import generator_util
import os
import re
import shlex
import subprocess

libsodium_config_opts = [
    "--enable-static",
    "--disable-shared",
]

subprocess.call(["./configure"] + libsodium_config_opts)

libraries = {
    "sodium": ["avx512f", "avx2", "sse41", "ssse3", "sse2", "aesni"],
    "avx512f": [],
    "avx2": [],
    "sse41": [],
    "ssse3": [],
    "sse2": [],
    "aesni": [],
}

# TODO(per-gron): This is not very nice; it assumes that the package is
# being imported with a given name.
external_dir = "external/libsodium/"

extra_cflags = [
    "-I%ssrc/libsodium/crypto_generichash/blake2b/ref" % external_dir,
    "-I%ssrc/libsodium/crypto_pwhash/argon2" % external_dir,
    "-I$(GENDIR)/%ssrc/libsodium/include/sodium" % external_dir,
    "-Wno-unknown-pragmas",
]

makefile = "src/libsodium/Makefile"

cflags_str = generator_util.extract_variable_from_makefile(
    "$(DEFS) $(libaesni_la_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)",
    makefile)
cflags = shlex.split(cflags_str)
# Claim to not have explicit_bzero even if we do have it, because it was
# introduced in glibc 2.25, which is much more recent than other symbols used
# (and thus unnecessarily makes the program not run on lots of Linuxes).
cflags = ["'%s'" % flag for flag in cflags if flag != "-g" and not re.match(r"^-O\d$", flag) and flag != "-DHAVE_EXPLICIT_BZERO=1" and not re.match(r"^-D_FORTIFY_SOURCE=", flag)]

version_h = "src/libsodium/include/sodium/version.h"

def process_library(name, deps):
    rule = ""

    def obj_to_src(obj):
        without_ext = "src/libsodium/" + re.sub(r"/lib" + name + r"_la-(.*)\.lo$", r"/\1", obj)
        for ext in [".S", ".c"]:
            candidate = "%s%s" % (without_ext, ext)
            if os.path.isfile(candidate):
                return candidate
        raise "Could not find file for %s" % without_ext

    objs = shlex.split(generator_util.extract_variable_from_makefile(
        "$(lib%s_la_OBJECTS)" % name, makefile))
    srcs = [obj_to_src(obj) for obj in objs] + [version_h]

    rule += "cc_library(\n"
    if name == "sodium":
        rule += '    visibility = ["//visibility:public"],\n'
        rule += '    hdrs = headers,\n'
    rule += "    name = '%s',\n" % name
    rule += "    copts = cflags,\n"
    rule += "    linkstatic = 1,\n"
    rule += "    includes = ['src/libsodium/include', 'src/libsodium/include/sodium'],\n"
    rule += "    deps = %s,\n" % [":%s" % dep for dep in deps]
    rule += "    srcs = %s + headers,\n" % srcs
    rule += "    textual_hdrs = assembly_files,\n"
    rule += ")\n\n"

    return rule

def process_libraries():
    res = ""
    for lib in libraries:
        res += process_library(lib, libraries[lib])
    return res

build_file = generator_util.build_header()
build_file += "cflags = %s\n" % (cflags + extra_cflags)
build_file += "headers = glob(['src/**/*.h'])\n"
build_file += "assembly_files = glob(['src/**/*.S'])\n\n"
build_file += process_libraries()
build_file += generator_util.copy_file_genrule(
    version_h, generator_util.read_file(version_h))

generator_util.write_file("BUILD.bazel", build_file)
