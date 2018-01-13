# TODO(per-gron): bitcoin-util-test.py

cc_library(
    name = "accounting_tests",
    alwayslink = 1,
    srcs = ["accounting_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "addrman_tests",
    alwayslink = 1,
    srcs = ["addrman_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:addrman",
        "//src:hash",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "alert_tests",
    alwayslink = 1,
    srcs = ["alert_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:alertkeys",
        "//src:clientversion",
        "//src:key",
        "//src:main",
        "//src:rpcprotocol",
        "//src:serialize",
        "//src:streams",
        "//src/test/data:alertTests",
        "//src:util",
        "//src:utilstrencodings",
        "@boost//:filesystem",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "allocator_tests",
    alwayslink = 1,
    srcs = ["allocator_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:util",
        "//src/support/allocators:secure",
        "@boost//:test",
    ],
)

cc_library(
    name = "arith_uint256_tests",
    alwayslink = 1,
    srcs = ["arith_uint256_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:arith_uint256",
        "//src:uint256",
        "//src:version",
        "@boost//:test",
    ],
)

cc_library(
    name = "base32_tests",
    alwayslink = 1,
    srcs = ["base32_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:utilstrencodings",
        "@boost//:test",
    ],
)

cc_library(
    name = "base58_tests",
    alwayslink = 1,
    srcs = ["base58_tests.cpp"],
    deps = [
        ":test_bitcoin",
        ":test_util",
        "//src:key",
        "//src:main",
        "//src:uint256",
        "//src:util",
        "//src:utilstrencodings",
        "//src/script",
        "//src/test/data:base58_encode_decode",
        "//src/test/data:base58_keys_invalid",
        "//src/test/data:base58_keys_valid",
        "//src/univalue",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "base64_tests",
    alwayslink = 1,
    srcs = ["base64_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:utilstrencodings",
        "@boost//:test",
    ],
)

cc_library(
    name = "bignum",
    alwayslink = 1,
    hdrs = ["bignum.h"],
    deps = [
        "@openssl//:crypto",
    ],
)

cc_library(
    name = "bip32_tests",
    alwayslink = 1,
    srcs = ["bip32_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:key",
        "//src:main",
        "//src:uint256",
        "//src:util",
        "//src:utilstrencodings",
        "@boost//:test",
    ],
)

cc_library(
    name = "bloom_tests",
    alwayslink = 1,
    srcs = ["bloom_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:bloom",
        "//src:clientversion",
        "//src:key",
        "//src:main",
        "//src:merkleblock",
        "//src:serialize",
        "//src:streams",
        "//src:uint256",
        "//src:util",
        "//src:utilstrencodings",
        "@boost//:test",
        "@boost//:tuple",
    ],
)

cc_library(
    name = "checkblock_tests",
    alwayslink = 1,
    srcs = ["checkblock_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:clientversion",
        "//src:main",
        "//src:utiltime",
        "//src/consensus:validation",
        "//src/zcash:Proof",
        "@boost//:filesystem",
        "@boost//:test",
    ],
)

cc_library(
    name = "coins_tests",
    alwayslink = 1,
    srcs = ["coins_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:hash",
        "//src:main",
        "//src:uint256",
        "//src:undo",
        "//src:util",
        "//src:utilstrencodings",
        "//src/consensus:validation",
        "//src/script:standard",
        "//src/zcash:IncrementalMerkleTree",
        "@boost//:test",
    ],
)

cc_library(
    name = "compress_tests",
    alwayslink = 1,
    srcs = ["compress_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:compressor",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "crypto_tests",
    alwayslink = 1,
    srcs = ["crypto_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:util",
        "//src:utilstrencodings",
        "//src/crypto:hmac_sha256",
        "//src/crypto:hmac_sha512",
        "//src/crypto:ripemd160",
        "//src/crypto:sha1",
        "//src/crypto:sha256",
        "//src/crypto:sha512",
        "@boost//:assign",
        "@boost//:test",
    ],
)

cc_library(
    name = "DoS_tests",
    alwayslink = 1,
    srcs = ["DoS_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:keystore",
        "//src:main",
        "//src:serialize",
        "//src:util",
        "//src/script:sign",
        "@boost//:assign",
        "@boost//:date_time",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "equihash_tests",
    alwayslink = 1,
    srcs = ["equihash_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:arith_uint256",
        "//src:uint256",
        "//src/config:bitcoin-config",
        "//src/crypto:equihash",
        "//src/crypto:sha256",
        "@boost//:test",
        "@libsodium//:sodium",
    ],
)

cc_library(
    name = "getarg_tests",
    alwayslink = 1,
    srcs = ["getarg_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:util",
        "@boost//:algorithm",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "hash_tests",
    alwayslink = 1,
    srcs = ["hash_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:hash",
        "//src:utilstrencodings",
        "@boost//:test",
    ],
)

cc_library(
    name = "key_tests",
    alwayslink = 1,
    srcs = ["key_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:key",
        "//src:main",
        "//src:uint256",
        "//src:util",
        "//src:utilstrencodings",
        "//src/script",
        "//src/zcash:Address",
        "@boost//:test",
    ],
)

cc_library(
    name = "main_tests",
    alwayslink = 1,
    srcs = ["main_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "@boost//:signals2",
        "@boost//:test",
    ],
)

cc_library(
    name = "mempool_tests",
    alwayslink = 1,
    srcs = ["mempool_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "miner_tests",
    alwayslink = 1,
    srcs = ["miner_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:arith_uint256",
        "//src:hash",
        "//src:main",
        "//src:uint256",
        "//src:util",
        "//src/consensus:validation",
        "//src/crypto:equihash",
        "@boost//:test",
    ],
)

cc_library(
    name = "mruset_tests",
    alwayslink = 1,
    srcs = ["mruset_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:mruset",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "multisig_tests",
    alwayslink = 1,
    srcs = ["multisig_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:key",
        "//src:keystore",
        "//src:main",
        "//src:uint256",
        "//src:wallet_wallet_ismine",
        "//src/script",
        "//src/script:interpreter",
        "//src/script:script_error",
        "//src/script:sign",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "netbase_tests",
    alwayslink = 1,
    srcs = ["netbase_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:netbase",
        "@boost//:assign",
        "@boost//:test",
    ],
)

cc_library(
    name = "pmt_tests",
    alwayslink = 1,
    srcs = ["pmt_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:arith_uint256",
        "//src:merkleblock",
        "//src:serialize",
        "//src:streams",
        "//src:uint256",
        "//src:util",
        "//src:version",
        "@boost//:assign",
        "@boost//:test",
    ],
)

cc_library(
    name = "policyestimator_tests",
    alwayslink = 1,
    srcs = ["policyestimator_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "//src:uint256",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "pow_tests",
    alwayslink = 1,
    srcs = ["pow_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "raii_event_tests",
    alwayslink = 1,
    srcs = ["raii_event_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src/support:events",
        "@boost//:test",
        "@libevent//:event",
    ],
)

cc_library(
    name = "reverselock_tests",
    alwayslink = 1,
    srcs = ["reverselock_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:reverselock",
        "@boost//:test",
    ],
)

cc_library(
    name = "rpc_tests",
    alwayslink = 1,
    srcs = ["rpc_tests.cpp"],
    deps = [
        ":test_bitcoin",
        ":test_util",
        "//src:main",
        "//src:netbase",
        "//src:rpcclient",
        "//src/univalue",
        "@boost//:algorithm",
        "@boost//:test",
    ],
)

cc_library(
    name = "rpc_wallet_tests",
    alwayslink = 1,
    srcs = ["rpc_wallet_tests.cpp"],
    deps = [
        ":test_bitcoin",
        ":test_util",
        "//src:asyncrpcoperation",
        "//src:asyncrpcqueue",
        "//src:main",
        "//src:rpcclient",
        "//src:rpcprotocol",
        "//src/univalue",
        "//src/zcash:Address",
        "@boost//:algorithm",
        "@boost//:filesystem",
        "@boost//:format",
        "@boost//:optional",
        "@boost//:test",
    ],
)

cc_library(
    name = "sanity_tests",
    alwayslink = 1,
    srcs = ["sanity_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:key",
        "//src/compat:sanity",
        "@boost//:test",
    ],
)

cc_library(
    name = "scheduler_tests",
    alwayslink = 1,
    srcs = ["scheduler_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:scheduler",
        "//src:util",
        "@boost//:bind",
        "@boost//:random",
        "@boost//:test",
        "@boost//:thread",
    ],
)

cc_library(
    name = "script_P2SH_tests",
    alwayslink = 1,
    srcs = ["script_P2SH_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:key",
        "//src:keystore",
        "//src:main",
        "//src:wallet_wallet_ismine",
        "//src/script",
        "//src/script:script_error",
        "//src/script:sign",
        "@boost//:test",
    ],
)

cc_library(
    name = "script_tests",
    alwayslink = 1,
    srcs = ["script_tests.cpp"],
    deps = [
        ":test_bitcoin",
        ":test_util",
        "//src:key",
        "//src:keystore",
        "//src:main",
        "//src:util",
        "//src/script",
        "//src/script:script_error",
        "//src/script:sign",
        "//src/script:zcashconsensus",
        "//src/test/data:script_invalid",
        "//src/test/data:script_valid",
        "//src/univalue",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "scriptnum_tests",
    alwayslink = 1,
    srcs = ["scriptnum_tests.cpp"],
    deps = [
        ":bignum",
        ":test_bitcoin",
        "//src/script",
        "@boost//:test",
    ],
)

cc_library(
    name = "serialize_tests",
    alwayslink = 1,
    srcs = ["serialize_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:hash",
        "//src:serialize",
        "//src:streams",
        "//src:utilstrencodings",
        "@boost//:optional",
        "@boost//:test",
    ],
)

cc_library(
    name = "sha256compress_tests",
    alwayslink = 1,
    srcs = ["sha256compress_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:uint256",
        "//src/crypto:sha256",
        "@boost//:test",
    ],
)

cc_library(
    name = "sighash_tests",
    alwayslink = 1,
    srcs = ["sighash_tests.cpp"],
    deps = [
        ":test_bitcoin",
        ":test_util",
        "//src:main",
        "//src:serialize",
        "//src:util",
        "//src:version",
        "//src/consensus:validation",
        "//src/script",
        "//src/script:interpreter",
        "//src/test/data:sighash",
        "//src/univalue",
        "@boost//:test",
        "@libsodium//:sodium",
    ],
)

cc_library(
    name = "sigopcount_tests",
    alwayslink = 1,
    srcs = ["sigopcount_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:hash",
        "//src:key",
        "//src:uint256",
        "//src/script",
        "//src/script:standard",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "skiplist_tests",
    alwayslink = 1,
    srcs = ["skiplist_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "//src:util",
        "@boost//:test",
    ],
)

cc_library(
    name = "test_bitcoin",
    visibility = ["//src/wallet/test:__pkg__"],
    hdrs = ["test_bitcoin.h"],
    srcs = ["test_bitcoin.cpp"],
    deps = [
        "//src:hash",
        "//src:key",
        "//src:main",
        "//src:ui_interface",
        "//src:util",
        "//src:wallet_db",
        "//src/crypto:common",
        "@boost//:filesystem",
        "@boost//:test",
        "@boost//:thread",
    ],
    data = [
        "@sprout-params//:sprout_proving_key",
        "@sprout-params//:sprout_verifying_key",
    ],
    copts = [
        "-DBAZEL_BUILD",
        r"-DSPROUT_PROVING_KEY=\"$(location @sprout-params//:sprout_proving_key)\"",
        r"-DSPROUT_VERIFYING_KEY=\"$(location @sprout-params//:sprout_verifying_key)\"",
    ],
)

cc_test(
    name = "bitcoin_tests",
    # NOTE(per-gron): The normal way of organizing tests in Bazel is to have one
    # cc_test rule for each test file. However, this code base's use of globals
    # is not compatible with dynamic linking (at least on Linux); it causes
    # double-free errors. A way to fix this is to make all tests linkstatic = 1.
    # That does not work well though because the size of all the test
    # executables is just huge and causes long linking times. To make this less
    # bad, I am grouping all the tests into a single executable. (This prevents
    # running the tests in parallel though, and will cause Bazel to run more
    # tests than strictly necessary on rebuilds).
    linkstatic = 1,
    deps = [
        ":accounting_tests",
        ":addrman_tests",
        ":alert_tests",
        ":allocator_tests",
        ":arith_uint256_tests",
        ":base32_tests",
        ":base58_tests",
        ":base64_tests",
        ":bip32_tests",
        ":bloom_tests",
        ":checkblock_tests",
        ":coins_tests",
        ":compress_tests",
        ":crypto_tests",
        ":DoS_tests",
        ":equihash_tests",
        ":getarg_tests",
        ":hash_tests",
        ":key_tests",
        ":main_tests",
        ":mempool_tests",
        ":miner_tests",
        ":mruset_tests",
        ":multisig_tests",
        ":netbase_tests",
        ":pmt_tests",
        ":policyestimator_tests",
        ":pow_tests",
        ":raii_event_tests",
        ":reverselock_tests",
        ":rpc_tests",
        ":rpc_wallet_tests",
        ":sanity_tests",
        ":scheduler_tests",
        ":script_P2SH_tests",
        ":script_tests",
        ":scriptnum_tests",
        ":serialize_tests",
        ":sha256compress_tests",
        ":sighash_tests",
        ":sigopcount_tests",
        ":skiplist_tests",
        ":timedata_tests",
        ":torcontrol_tests",
        ":transaction_tests",
        ":uint256_tests",
        ":univalue_tests",
        ":util_tests",
    ]
)

cc_library(
    name = "test_util",
    alwayslink = 1,
    visibility = ["//src/wallet/test:__pkg__"],
    hdrs = ["test_util.h"],
    srcs = ["test_util.cpp"],
    deps = [
        "//src:main",
        "//src:rpcclient",
        "//src/script:interpreter",
        "//src/univalue",
        "@boost//:algorithm",
        "@boost//:assign",
        "@boost//:foreach",
        "@boost//:test",
    ],
)

cc_library(
    name = "timedata_tests",
    alwayslink = 1,
    srcs = ["timedata_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:timedata",
        "@boost//:test",
    ],
)

cc_library(
    name = "torcontrol_tests",
    alwayslink = 1,
    srcs = ["torcontrol_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:main",
        "@boost//:test",
    ],
)

cc_library(
    name = "transaction_tests",
    alwayslink = 1,
    srcs = ["transaction_tests.cpp"],
    deps = [
        ":test_bitcoin",
        ":test_util",
        "//src:clientversion",
        "//src:key",
        "//src:keystore",
        "//src:main",
        "//src/consensus:validation",
        "//src/primitives:transaction",
        "//src/script",
        "//src/script:script_error",
        "//src/test/data:tx_invalid",
        "//src/test/data:tx_valid",
        "//src/univalue",
        "//src/zcash:Address",
        "//src/zcash:Note",
        "//src/zcash:Proof",
        "@boost//:test",
        "@libsodium//:sodium",
    ],
)

cc_library(
    name = "uint256_tests",
    alwayslink = 1,
    srcs = ["uint256_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:arith_uint256",
        "//src:uint256",
        "//src:version",
        "@boost//:test",
    ],
)

cc_library(
    name = "univalue_tests",
    alwayslink = 1,
    srcs = ["univalue_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src/univalue",
        "@boost//:test",
    ],
)

cc_library(
    name = "util_tests",
    alwayslink = 1,
    srcs = ["util_tests.cpp"],
    deps = [
        ":test_bitcoin",
        "//src:clientversion",
        "//src:util",
        "//src:utilmoneystr",
        "//src:utilstrencodings",
        "//src/primitives:transaction",
        "@boost//:test",
    ],
)
