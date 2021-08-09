from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.3",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the cunt processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="cunt-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@cuntnetwork.net",
    description="Cunt blockchain full node, farmer, timelord, and wallet.",
    url="https://cuntnetwork.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="cunt blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "cunt",
        "cunt.cmds",
        "cunt.clvm",
        "cunt.consensus",
        "cunt.daemon",
        "cunt.full_node",
        "cunt.timelord",
        "cunt.farmer",
        "cunt.harvester",
        "cunt.introducer",
        "cunt.plotting",
        "cunt.pools",
        "cunt.protocols",
        "cunt.rpc",
        "cunt.server",
        "cunt.simulator",
        "cunt.types.blockchain_format",
        "cunt.types",
        "cunt.util",
        "cunt.wallet",
        "cunt.wallet.puzzles",
        "cunt.wallet.rl_wallet",
        "cunt.wallet.cc_wallet",
        "cunt.wallet.did_wallet",
        "cunt.wallet.settings",
        "cunt.wallet.trading",
        "cunt.wallet.util",
        "cunt.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "cunt = cunt.cmds.cunt:main",
            "cunt_wallet = cunt.server.start_wallet:main",
            "cunt_full_node = cunt.server.start_full_node:main",
            "cunt_harvester = cunt.server.start_harvester:main",
            "cunt_farmer = cunt.server.start_farmer:main",
            "cunt_introducer = cunt.server.start_introducer:main",
            "cunt_timelord = cunt.server.start_timelord:main",
            "cunt_timelord_launcher = cunt.timelord.timelord_launcher:main",
            "cunt_full_node_simulator = cunt.simulator.start_simulator:main",
        ]
    },
    package_data={
        "cunt": ["pyinstaller.spec"],
        "cunt.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "cunt.util": ["initial-*.yaml", "english.txt"],
        "cunt.ssl": ["cunt_ca.crt", "cunt_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
