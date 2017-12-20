"""Generates a BUILD.bazel file suitable for ZCash given a libevent source
directory. Run this script in the libevent source directory. It creates a
BUILD.bazel file there.
"""
import os
import subprocess
import glob
import pprint
import generator_util

libevent_config_opts = [
    "--disable-shared",
    "--disable-openssl",
    "--disable-libevent-regress",
    "--with-pic",
]

subprocess.call(["./autogen.sh"])
subprocess.call(["./configure"] + libevent_config_opts)

with open("Makefile", "a") as makefile:
    makefile.write("echo_srcs:\n\t@echo $(libevent_la_SOURCES)\n")
    makefile.write("echo_cflags:\n\t@echo $(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CFLAGS) $(CFLAGS)\n")

subprocess.call(["make", "include/event2/event-config.h"])
subprocess.call(["make", "evconfig-private.h"])

srcs = subprocess.check_output(["make", "echo_srcs"])
cflags = subprocess.check_output(["make", "echo_cflags"])

generated_headers = {
    "include/event2/event-config.h": generator_util.read_file("include/event2/event-config.h"),
    "evconfig-private.h": generator_util.read_file("evconfig-private.h"),
}

def process_generated_header(generated_header, src):
    name = generated_header.replace('.', '_').replace('/', '_').replace('-', '_')

    rule = ""
    rule += "%s_contents = r\"\"\"%s\"\"\"\n" % (name, src)
    rule += "genrule(\n"
    rule += "  name = '%s',\n" % name
    rule += "  outs = ['%s'],\n" % generated_header
    rule += "  cmd = \"cat > $@ << 'BAZEL_EOF'\\n\" + %s_contents.replace('$', '$$') + \"\\nBAZEL_EOF\",\n" % name
    rule += ")\n\n"

    return rule

build_file = generator_util.build_header()
build_file = ("""
cc_library(
  visibility = ["//visibility:public"],
  includes = [
    "include",
  ],
  copts = %s + [
    "-DHAVE_CONFIG_H",
    "-w",  # Silence "warning: comparison between pointer and integer"
  ],
  srcs = glob(["*.h"]) + [
    "include/event2/event-config.h",
    "evconfig-private.h",
  ] + %s,
  textual_hdrs = [
    "arc4random.c",
    "epoll_sub.c",
  ],
  hdrs = glob(["include/**/*.h"]),
  name = "event",
)

""" % (cflags.split(), pprint.pformat(srcs.split())))

for generated_header in generated_headers:
    build_file += process_generated_header(generated_header, generated_headers[generated_header])

with open("BUILD.bazel", "w") as bazel:
    bazel.write(build_file)
