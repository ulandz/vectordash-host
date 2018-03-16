import click

from vdhost.cli.setcommands import setcommands
from vdhost.cli.mine import mine
from vdhost.cli.stop import stop


@click.group()
def cli():
    """
    Vectordash CLI interacts with Vectordash server and executes your commands.
    More help is available under each command listed below.
    """
    pass


def add_commands(cli):
    cli.add_command(setcommands)
    cli.add_command(mine)
    cli.add_command(stop)


add_commands(cli)
