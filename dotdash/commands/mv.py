"""This module contains the mv command and its functions."""
import click


@click.command()
@click.argument(
    "source",
    required=True,
    type=click.Path(exists=True),
)
@click.argument(
    "target",
    required=True,
    type=click.Path(),
)
def mv(source, target):
    """Move the symlink, file or directory SOURCE in a synced fasion.

    Symlinks and dotfiles will be updated to reflect changes.
    """
    click.echo(f"Move {source}, {target}")
