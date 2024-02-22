"""Common helper functions."""
import os
from typing import Dict
from pathlib import Path

from dotenv import dotenv_values


CONFIG_VALUES = [
    "DOTFILES"
]

CONFIG_DEFAULT = Path.home() / ".dotfiles-dir"

def get_config() -> Dict:
    """Return configuration values from all sources."""
    config = {}

    config_values = {
        **dotenv_values(Path.home() / ".dotdash/config"),
        **dotenv_values(Path.home() / ".config/dotdash/config"),
        **dotenv_values(CONFIG_DEFAULT),
        **os.environ,
    }

    for key in CONFIG_VALUES:
        if key in config_values.keys():
            config[key] = config_values[key]

    return config
