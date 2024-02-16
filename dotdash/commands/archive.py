import click


@click.command()
@click.argument(
    "filename",
    required=False,
    type=click.Path(writable=True),
)
def archive(filename):
    """Archive dotfiles dir to FILENAME. Default is dotfiles-{date}.tar.gz."""
    click.echo(f"Archive {click.format_filename(filename)}")
