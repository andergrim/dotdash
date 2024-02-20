"""Console script for dotdash."""
import importlib
import re
from pathlib import Path

import click

from dotdash.dotdash import get_config


COMMAND_PATH = Path("dotdash/commands/")
CONFIG = get_config()
DOTFILES = CONFIG.get("DOTFILES")

if not DOTFILES:
    epilog = click.style(
        "No dotfiles directory initialized, use dotdash init",
        fg="red"
    )
    DOTFILES_FULL = None
else:
    DOTFILES_FULL = Path(DOTFILES).expanduser()
    epilog = ""

if DOTFILES_FULL and DOTFILES_FULL.exists():
    epilog = click.style(
        f"Dotfiles directory is {DOTFILES}",
        fg="green"
    )
elif DOTFILES_FULL:
    epilog = click.style(
        f"Configured directory {DOTFILES} does not exist",
        fg="red"
    )

@click.group(epilog=epilog)
@click.version_option()
def main():
    pass


if __name__ == "__main__":
    main()  # pragma: no cover

for mod_path in COMMAND_PATH.glob("*.py"):
    mod_name = re.sub(f"/", ".", str(mod_path)).rpartition(".py")[0]
    mod = importlib.import_module(mod_name)

    for attr in dir(mod):
        foo = getattr(mod, attr)
        if callable(foo) and type(foo) is click.core.Command:
            main.add_command(foo)
