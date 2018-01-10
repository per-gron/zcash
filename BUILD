cc_binary(
    name = "hello",
    srcs = ["hello.cc"],
    deps = [
        "@boost//:thread",
        "@openssl//:crypto",
        "@openssl//:ssl",
        "@com_google_googletest//:gtest",
        "@bdb//:db_cxx",
        "@libevent//:event",
        "@libgmp//:gmp",
        "@libsodium//:sodium",
        "@zeromq//:zmq",
        "@proton//:qpid-proton-cpp",
    ]
)

cc_binary(
    name = "minimal",
    srcs = ["minimal.cc"],
)

load("@io_bazel_rules_rust//rust:rust.bzl", "rust_binary")

rust_binary(
    name = "hello_rust",
    srcs = ["hello_rust.rs"],
)
