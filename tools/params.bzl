def _fetch_sprout_params_impl(repository_ctx):
    repository_ctx.download(
        "https://z.cash/downloads/sprout-proving.key",
        output = 'sprout-proving.key',
        sha256 = '8bc20a7f013b2b58970cddd2e7ea028975c88ae7ceb9259a5344a16bc2c0eef7',
    )
    repository_ctx.download(
        "https://z.cash/downloads/sprout-verifying.key",
        output = 'sprout-verifying.key',
        sha256 = '4bd498dae0aacfd8e98dc306338d017d9c08dd0918ead18172bd0aec2fc5df82',
    )

fetch_sprout_params = repository_rule(
    implementation = _fetch_sprout_params_impl,
)
