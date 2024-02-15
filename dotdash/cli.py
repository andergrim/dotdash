"""Console script for dotdash."""

import click


@click.group()
@click.version_option()
def main():
    pass


@click.command()
@click.argument("dir",
                required=False,
                type=click.Path(exists=True),
)
def init(dir):
    """Initialize directory DIR as your dotfiles directory. Default is CWD."""

    if not dir:
        dir = "."  # CWD

    click.echo(f"Init {dir}")


@click.command()
@click.argument("path",
                required=True,
                type=click.Path(exists=True),
)
def adopt(path):
    """Move file or directory PATH to dotfiles dir, replacing it with a symlink.
    """
    click.echo(f"Adopt {click.format_filename(path)}")


@click.command()
@click.argument("path",
                required=True,
                type=click.Path(exists=True),
)
def evict(path):
    """Move file or directory PATH back to its original location."""
    click.echo(f"Evict {click.format_filename(path)}")


@click.command()
@click.argument("source",
                required=True,
                type=click.Path(exists=True),
)
@click.argument("target",
                required=True,
                type=click.Path(),
)
def mv(source, target):
    ## TODO! Alias move
    """Move the symlink, file or directory SOURCE, updating the filesystem to
    reflect the changes.
    """
    click.echo(f"Move {source}, {target}")


@click.command()
@click.argument("filename",
                required=False,
                type=click.Path(writable=True),
)
def archive(filename):
    """Archive dotfiles dir to FILENAME. Default is dotfiles-{date}.tar.gz."""
    click.echo(f"Archive {click.format_filename(filename)}")


@click.command()
@click.option("force", "--force", flag_value=True, help="Force reset")
def reset(force=False):
    """Remove all symlinks created by dotdash."""
    click.echo(f"Reset {force}")


@click.command()
@click.argument("path",
                required=False,
                type=click.Path(exists=True),
)
@click.option("force", "--force", flag_value=True, help="Force synchronization")
@click.option("skip_git", "--skip-git", flag_value=True, help="Skip Git pull, commit, push")
def sync(path, force=False, skip_git=False):
    """Make sure all symlinks are correct, update and commit to Git."""
    click.echo(f"Sync {path}, {force}, {skip_git}")


@click.command()
def check():
    """Preform a health-check and print results."""
    click.echo("Check")


if __name__ == "__main__":
    main()  # pragma: no cover

main.add_command(init)
main.add_command(sync)
main.add_command(check)
main.add_command(archive)
main.add_command(reset)
main.add_command(adopt)
main.add_command(evict)
main.add_command(mv)
