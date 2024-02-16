"""Console script for dotdash."""
import importlib
import re
from pathlib import Path

import click


COMMAND_PATH = Path("dotdash/commands/")

@click.group()
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
