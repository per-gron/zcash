test_data = [
    "//src:zcashd",
    "//src:zcash-cli",
    "@sprout-params//:sprout_proving_key",
    "@sprout-params//:sprout_verifying_key",
]

test_args = [
    "--testbinary=$(location //src:zcashd)",
    "--clibinary=$(location //src:zcash-cli)",
    "--sprout-proving-key=$(location @sprout-params//:sprout_proving_key)",
    "--sprout-verifying-key=$(location @sprout-params//:sprout_verifying_key)",
]

py_test(
    name = "paymentdisclosure",
    srcs = ["paymentdisclosure.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "prioritisetransaction",
    srcs = ["prioritisetransaction.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:mininode",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "wallet_treestate",
    srcs = ["wallet_treestate.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "wallet_protectcoinbase",
    srcs = ["wallet_protectcoinbase.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "wallet_shieldcoinbase",
    srcs = ["wallet_shieldcoinbase.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "wallet",
    srcs = ["wallet.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "wallet_nullifiers",
    srcs = ["wallet_nullifiers.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "wallet_1941",
    srcs = ["wallet_1941.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "listtransactions",
    srcs = ["listtransactions.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "mempool_resurrect_test",
    srcs = ["mempool_resurrect_test.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "txn_doublespend",
    srcs = ["txn_doublespend.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "txn_doublespend_mineblock",
    main = "txn_doublespend.py",
    srcs = ["txn_doublespend.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = ["--mineblock"] + test_args,
)

py_test(
    name = "getchaintips",
    srcs = ["getchaintips.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "rawtransactions",
    srcs = ["rawtransactions.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "rest",
    srcs = ["rest.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "mempool_spendcoinbase",
    srcs = ["mempool_spendcoinbase.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "mempool_coinbase_spends",
    srcs = ["mempool_coinbase_spends.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "mempool_tx_input_limit",
    srcs = ["mempool_tx_input_limit.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "httpbasics",
    srcs = ["httpbasics.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "zapwallettxes",
    srcs = ["zapwallettxes.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "proxy_test",
    srcs = ["proxy_test.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:socks5",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "merkle_blocks",
    srcs = ["merkle_blocks.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "fundrawtransaction",
    srcs = ["fundrawtransaction.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "signrawtransactions",
    srcs = ["signrawtransactions.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "walletbackup",
    srcs = ["walletbackup.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "key_import_export",
    srcs = ["key_import_export.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "nodehandling",
    srcs = ["nodehandling.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "reindex",
    srcs = ["reindex.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "decodescript",
    srcs = ["decodescript.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "disablewallet",
    srcs = ["disablewallet.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "zcjoinsplit",
    srcs = ["zcjoinsplit.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "zcjoinsplitdoublespend",
    srcs = ["zcjoinsplitdoublespend.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "zkey_import_export",
    srcs = ["zkey_import_export.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "getblocktemplate",
    srcs = ["getblocktemplate.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "bip65_cltv_p2p",
    srcs = ["bip65-cltv-p2p.py"],
    main = "bip65-cltv-p2p.py",
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:blocktools",
        "//qa/rpc_tests/test_framework:comptool",
        "//qa/rpc_tests/test_framework:mininode",
        "//qa/rpc_tests/test_framework:script",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "bipdersig_p2p",
    srcs = ["bipdersig-p2p.py"],
    main = "bipdersig-p2p.py",
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:blocktools",
        "//qa/rpc_tests/test_framework:comptool",
        "//qa/rpc_tests/test_framework:mininode",
        "//qa/rpc_tests/test_framework:script",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_getblocktemplate_longpoll",
    main = "getblocktemplate_longpoll.py",
    srcs = ["getblocktemplate_longpoll.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_getblocktemplate_proposals",
    main = "getblocktemplate_proposals.py",
    srcs = ["getblocktemplate_proposals.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_pruning",
    main = "pruning.py",
    srcs = ["pruning.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_forknotify",
    main = "forknotify.py",
    srcs = ["forknotify.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_hardforkdetection",
    main = "hardforkdetection.py",
    srcs = ["hardforkdetection.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_invalidateblock",
    main = "invalidateblock.py",
    srcs = ["invalidateblock.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_keypool",
    main = "keypool.py",
    srcs = ["keypool.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_receivedby",
    main = "receivedby.py",
    srcs = ["receivedby.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_rpcbind_test",
    main = "rpcbind_test.py",
    srcs = ["rpcbind_test.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework:authproxy",
        "//qa/rpc_tests/test_framework:netutil",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

# py_test(
#     name = "ext_script_test",
#     main = "script_test.py",
#     srcs = ["script_test.py"],
#     timeout = "long",
#     deps = [
#         "//qa/rpc_tests/test_framework",
#         "//qa/rpc_tests/test_framework:blocktools",
#         "//qa/rpc_tests/test_framework:comptool",
#         "//qa/rpc_tests/test_framework:mininode",
#         "//qa/rpc_tests/test_framework:script",
#     ],
#     data = test_data,
#     args = test_args,
# )

py_test(
    name = "ext_smartfees",
    main = "smartfees.py",
    srcs = ["smartfees.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_maxblocksinflight",
    main = "maxblocksinflight.py",
    srcs = ["maxblocksinflight.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:mininode",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

py_test(
    name = "ext_invalidblockrequest",
    main = "invalidblockrequest.py",
    srcs = ["invalidblockrequest.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:blocktools",
        "//qa/rpc_tests/test_framework:comptool",
        "//qa/rpc_tests/test_framework:mininode",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)

# py_test(
#     name = "ext_forknotify",
#     main = "forknotify.py",
#     srcs = ["forknotify.py"],
#     timeout = "long",
#     deps = [
#         "//qa/rpc_tests/test_framework",
#         "//qa/rpc_tests/test_framework:util",
#     ],
#     data = test_data,
#     args = test_args,
# )

py_test(
    name = "ext_p2p",
    main = "p2p-acceptblock.py",
    srcs = ["p2p-acceptblock.py"],
    timeout = "long",
    deps = [
        "//qa/rpc_tests/test_framework",
        "//qa/rpc_tests/test_framework:blocktools",
        "//qa/rpc_tests/test_framework:mininode",
        "//qa/rpc_tests/test_framework:util",
    ],
    data = test_data,
    args = test_args,
)
