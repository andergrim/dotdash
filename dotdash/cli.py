"""Console script for dotdash."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("dotdash")
    click.echo("=" * len("dotdash"))
    click.echo("Flexible dotfile keeper")


if __name__ == "__main__":
    main()  # pragma: no cover
