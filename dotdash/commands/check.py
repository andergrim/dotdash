"""This module contains the check command and its functions."""
import click


@click.command()
def check():
    """Preform a health-check and print results."""
    click.echo("Check")


