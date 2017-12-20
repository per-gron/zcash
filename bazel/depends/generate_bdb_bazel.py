"""Generates a BUILD.bazel file suitable for ZCash given a bdb source
directory. Run this script in the bdb source directory. It creates a
BUILD.bazel file there.
"""
import os
import subprocess
import glob
import pprint
import generator_util

bdb_config_opts = [
    "--disable-shared",
    "--enable-cxx",
    "--disable-replication",
    "--with-pic",
]

os.chdir("build_unix")
subprocess.call(["../dist/configure"] + bdb_config_opts)

with open("Makefile", "a") as makefile:
    makefile.write("echo_c_objs:\n\t@echo $(C_OBJS)\n")
    makefile.write("echo_cxx_objs:\n\t@echo $(CXX_OBJS)\n")

c_objs = subprocess.check_output(["make", "echo_c_objs"])
cxx_objs = subprocess.check_output(["make", "echo_cxx_objs"])

generated_headers_dir = 'genheaders'
generated_headers = {
    'db_int.h': generator_util.read_file('db_int.h'),
    'db.h': generator_util.read_file('db.h'),
    'db_cxx.h': generator_util.read_file('db_cxx.h'),
    'clib_port.h': r"""
#include <limits.h>

#define INT64_FMT   "%ld"
#define UINT64_FMT  "%lu"
""",
    'db_config.h': generator_util.read_file('db_config.h'),
}

all_files = {}
for file in subprocess.check_output(["find", ".."]).split("\n"):
    (name, ext) = os.path.splitext(os.path.basename(file))
    if (ext == '.c' or ext == '.cpp') and ('os_windows' not in file and 'os_qnx' not in file and 'os_vxworks' not in file):
        all_files[name] = file.replace('../', '')

def obj_to_path(obj):
    name = obj.replace(".o", "").strip()
    return all_files[name]

def process_lib(lib_name, objs, hdrs, deps):
    srcs = [obj_to_path(obj) for obj in objs.split(" ")]    
    header_paths = ["%s/%s" % (generated_headers_dir, header) for header in generated_headers.keys()]

    rule = ""
    rule += "cc_library(\n"
    rule += "  name = '%s',\n" % lib_name
    rule += "  copts = cflags,\n"
    rule += "  linkopts = lflags,\n"
    rule += "  visibility = ['//visibility:public'],\n"
    rule += "  includes = ['%s'],\n" % generated_headers_dir
    rule += "  hdrs = %s + %s,\n" % (pprint.pformat(header_paths), hdrs)
    rule += "  srcs = %s,\n" % pprint.pformat(srcs)
    rule += "  deps = %s,\n" % pprint.pformat(deps)
    rule += ")\n\n"

    return rule

# TODO(per-gron): This is not very nice; it assumes that the package is
# being imported with a given name.
external_dir = "external/bdb/"

build_file = generator_util.build_header()
build_file += """
cflags = [
  "-D_GNU_SOURCE",
  "-D_REENTRANT",
  "-O3",
  "-I{{EXTERNAL_DIR}}src",
  "-Wno-unused-but-set-variable",
  "-Wno-strict-aliasing",
  "-Wno-maybe-uninitialized",
]
lflags = ["-lpthread"]

""".replace("{{EXTERNAL_DIR}}", external_dir)

for generated_header in generated_headers:
    build_file += generator_util.copy_file_genrule(generated_headers_dir + "/" + generated_header, generated_headers[generated_header])

build_file += process_lib("db", c_objs, 'glob(["src/**/*.h", "src/**/*.incl"])', [])
build_file += process_lib("db_cxx", c_objs, '[]', [":db"])

with open("../BUILD.bazel", "w") as bazel:
    bazel.write(build_file)
