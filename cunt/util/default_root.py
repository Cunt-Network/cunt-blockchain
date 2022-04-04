import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("CUNT_ROOT", "~/.cunt/mainnet"))).resolve()
STANDALONE_ROOT_PATH = Path(
    os.path.expanduser(os.getenv("CUNT_STANDALONE_WALLET_ROOT", "~/.cunt/standalone_wallet"))
).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("CUNT_KEYS_ROOT", "~/.cunt_keys"))).resolve()
