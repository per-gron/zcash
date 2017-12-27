http_archive(
  name = "io_bazel_rules_rust",
  sha256 = "5cf8b372e1c61bc42e7975fe1deb05daea9c2005a29f1dacbe423cb9a709c0a8",
  strip_prefix = "bazelbuild-rules_rust-674dcd9",
  type = "tar.gz",
  urls = ["https://api.github.com/repos/bazelbuild/rules_rust/tarball/674dcd95ac8f7f5c67fbbfaada5ae558cc456b2c"],
)
load("@io_bazel_rules_rust//rust:repositories.bzl", "rust_repositories")
rust_repositories()

new_http_archive(
  name = "bdb",
  strip_prefix = "db-6.2.23",
  urls = ["http://download.oracle.com/berkeley-db/db-6.2.23.tar.gz"],
  sha256 = "47612c8991aa9ac2f6be721267c8d3cdccf5ac83105df8e50809daea24e95dc7",
  build_file = "bazel/depends/generated/bdb.bazel",
)

http_archive(
  name = "com_github_nelhage_boost",
  strip_prefix = "rules_boost-d19a448592c5818dc547e6a3ddda39a50c393b16",
  urls = ["https://github.com/nelhage/rules_boost/archive/d19a448592c5818dc547e6a3ddda39a50c393b16.tar.gz"],
  sha256 = "28cbed93a399711de1637837adde71e5519946b7ed1fec18f487d6b5fc493280",
)
load("@com_github_nelhage_boost//:boost/boost.bzl", "boost_deps")
boost_deps()

http_archive(
  name = "com_google_googletest",
  strip_prefix = "googletest-0fe96607d85cf3a25ac40da369db62bbee2939a5",
  urls = ["https://github.com/google/googletest/archive/0fe96607d85cf3a25ac40da369db62bbee2939a5.tar.gz"],
  sha256 = "80532b7a9c62945eed127a9cfa502f4b9f4af2a0c2329146026fd423e539f578",
)

new_http_archive(
  name = "libevent",
  strip_prefix = "libevent-release-2.1.8-stable",
  urls = ["https://github.com/libevent/libevent/archive/release-2.1.8-stable.tar.gz"],
  sha256 = "316ddb401745ac5d222d7c529ef1eada12f58f6376a66c1118eee803cb70f83d",
  build_file = "bazel/depends/generated/libevent.bazel",
)

new_http_archive(
  name = "libgmp",
  strip_prefix = "gmp-6.1.1",
  urls = ["https://gmplib.org/download/gmp/gmp-6.1.1.tar.bz2"],
  sha256 = "a8109865f2893f1373b0a8ed5ff7429de8db696fc451b1036bd7bdf95bbeffd6",
  build_file = "bazel/depends/generated/libgmp.bazel",
)

# TODO: librustzcash

new_http_archive(
  name = "libsodium",
  strip_prefix = "libsodium-1.0.15",
  urls = ["https://download.libsodium.org/libsodium/releases/libsodium-1.0.15.tar.gz"],
  sha256 = "fb6a9e879a2f674592e4328c5d9f79f082405ee4bb05cb6e679b90afe9e178f4",
  build_file = "bazel/depends/generated/libsodium.bazel",
)

new_http_archive(
  name = "openssl",
  strip_prefix = "openssl-1.1.0d",
  urls = ["https://www.openssl.org/source/openssl-1.1.0d.tar.gz"],
  sha256 = "7d5ebb9e89756545c156ff9c13cf2aa6214193b010a468a3bc789c3c28fe60df",
  build_file = "bazel/depends/generated/openssl.bazel",
)

new_http_archive(
  name = "py_appdirs",
  strip_prefix = "appdirs-1.4.3",
  urls = ["https://github.com/ActiveState/appdirs/archive/1.4.3.tar.gz"],
  sha256 = "5ce44e43c3fd537ce1aaf72141c525aa67032a5af0a14dcf755621e69d72414b",
  build_file_content = r"""
py_library(
  name = "py_appdirs",
  visibility = ["//visibility:public"],
  srcs = ["appdirs.py"],
)
""",
)

new_http_archive(
  name = "py_baron",
  strip_prefix = "baron-0.6.6",
  urls = ["https://github.com/PyCQA/baron/archive/0.6.6.tar.gz"],
  sha256 = "86ea5a7082138ef4c77564c11728d83f8c622cddfabcd44d0468c93e64318ce9",
  build_file_content = r"""
py_library(
  name = "py_baron",
  visibility = ["//visibility:public"],
  srcs = glob(["baron/*.py"]),
  deps = [
    "@py_rply//:py_rply",
  ],
)
""",
)

new_http_archive(
  name = "py_redbaron",
  strip_prefix = "redbaron-0.6.3",
  urls = ["https://github.com/PyCQA/redbaron/archive/0.6.3.tar.gz"],
  sha256 = "314cbcf442af55b06544fa0aec15991a94f88595d2b6b61e8d92bda7005a1400",
  build_file_content = r"""
py_library(
  name = "py_redbaron",
  visibility = ["//visibility:public"],
  srcs = glob(["redbaron/*.py"]),
  deps = [
    "@py_baron//:py_baron",
  ],
)
""",
)

new_http_archive(
  name = "py_rply",
  strip_prefix = "rply-0.7.5",
  urls = ["https://github.com/alex/rply/archive/v0.7.5.tar.gz"],
  sha256 = "a772cddc9cd648961d394749507d67e95498670ef9dd4a461617bb7b51d5eafc",
  build_file_content = r"""
py_library(
  name = "py_rply",
  visibility = ["//visibility:public"],
  srcs = glob(["rply/*.py"]),
  deps = [
    "@py_appdirs//:py_appdirs",
  ],
)
""",
)

new_http_archive(
  name = "proton",
  strip_prefix = "qpid-proton-0.17.0",
  urls = ["http://apache.cs.utah.edu/qpid/proton/0.17.0/qpid-proton-0.17.0.tar.gz"],
  sha256 = "6ffd26d3d0e495bfdb5d9fefc5349954e6105ea18cc4bb191161d27742c5a01a",
  build_file = "bazel/depends/generated/proton.bazel",
)

new_http_archive(
  name = "zeromq",
  strip_prefix = "zeromq-4.2.1",
  urls = ["https://github.com/zeromq/libzmq/releases/download/v4.2.1/zeromq-4.2.1.tar.gz"],
  sha256 = "27d1e82a099228ee85a7ddb2260f40830212402c605a4a10b5e5498a7e0e9d03",
  build_file = "bazel/depends/generated/zeromq.bazel",
)
