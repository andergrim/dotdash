import click


@click.command()
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=True),
)
def adopt(path):
    """Move file or directory PATH to dotfiles dir, replacing it with a symlink."""
    click.echo(f"Adopt {click.format_filename(path)}")
