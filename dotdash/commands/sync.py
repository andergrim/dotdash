import click


@click.command()
@click.argument(
    "path",
    required=False,
    type=click.Path(exists=True),
)
@click.option("force", "--force", flag_value=True, help="Force synchronization")
@click.option("skip_git", "--skip-git", flag_value=True, help="Skip Git pull, commit, push")
def sync(path, force=False, skip_git=False):
    """Make sure all symlinks are correct, update and commit to Git."""
    click.echo(f"Sync {path}, {force}, {skip_git}")

