# TODO: bdb

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
    name = "openssl",
    strip_prefix = "openssl-1.1.0d",
    urls = ["https://www.openssl.org/source/openssl-1.1.0d.tar.gz"],
    sha256 = "7d5ebb9e89756545c156ff9c13cf2aa6214193b010a468a3bc789c3c28fe60df",
    build_file = "bazel/openssl/openssl.bazel",
)

# TODO: libevent
# TODO: libgmp
# TODO: librustzcash
# TODO: libsodium
# TODO: openssl : https://github.com/bazelment/trunk/tree/master/third_party/openssl ?
# TODO: rust
# TODO: zeromq
