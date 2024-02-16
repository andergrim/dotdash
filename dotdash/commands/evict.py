import click


@click.command()
@click.argument(
    "path",
    required=True,
    type=click.Path(exists=True),
)
def evict(path):
    """Move file or directory PATH back to its original location."""
    click.echo(f"Evict {click.format_filename(path)}")

