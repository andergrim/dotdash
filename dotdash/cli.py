"""Console script for dotdash."""

import click


@click.group()
def main():
    pass

@click.command()
def init():
    click.echo("Init")

@click.command()
def sync():
    click.echo("Sync")

@click.command()
def check():
    click.echo("Check")

@click.command()
def archive():
    click.echo("Archive")

@click.command()
def reset():
    click.echo("reset")

@click.command()
def adopt():
    click.echo("Adopt")

@click.command()
def evict():
    click.echo("Evict")

@click.command()
def mv():
    click.echo("Move")



@click.command()
def sync():
    click.echo("Sync")

if __name__ == "__main__":
    main()  # pragma: no cover
