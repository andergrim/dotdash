"""This module contains the init command and its functions."""
import click


@click.command()
@click.argument(
    "dir",
    required=False,
    type=click.Path(exists=True),
)
def init(dir):
    """Initialize directory DIR as your dotfiles directory.

    Default is CWD.
    """
    if not dir:
        dir = "."  # CWD

    click.echo(f"Init {dir}")
