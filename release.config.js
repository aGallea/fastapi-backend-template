module.exports = {
    // https://github.com/semantic-release/semantic-release/blob/master/docs/extending/plugins-list.md
    plugins: [
        ["@semantic-release/commit-analyzer", {
            preset: "conventionalcommits"
        }],
        ["@semantic-release/release-notes-generator", {
            preset: "conventionalcommits"
        }],
        [
            "@semantic-release/changelog",
            {
                changelogTitle: `<!-- markdownlint-configure-file {"MD024": { "siblings_only": true }, "MD012": false } -->
# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).`,
            },
        ],
        ["@semantic-release/git", {
            assets: [
                "CHANGELOG.md"
            ],
            message: "chore(release): ${nextRelease.version} ${nextRelease.notes}"
        }],
        ["@semantic-release/github", {
            successComment:
                ":tada: This ${issue.pull_request ? 'pull request' : 'issue'} is included in [version ${nextRelease.version}](${releases.filter(release => /github\.com/i.test(release.url))[0].url}) :tada:",
            assets: ["*.tgz"],
        }]
    ],
    branches: [
        'master',
        {name: 'beta', prerelease: true}]
};
