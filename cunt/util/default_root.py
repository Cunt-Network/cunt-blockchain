import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("CUNT_ROOT", "~/.cunt/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("CUNT_KEYS_ROOT", "~/.cunt_keys"))).resolve()
