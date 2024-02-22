"""This module contains the reset command and its functions."""
import click


@click.command()
@click.option("force", "--force", flag_value=True, help="Force reset")
def reset(force=False):
    """Remove all symlinks created by dotdash."""
    click.echo(f"Reset {force}")
