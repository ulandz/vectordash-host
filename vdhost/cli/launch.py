import click
import subprocess
import os

from colored import fg
from colored import stylize


@click.command()
def launch():
    """
    args: None |
    Runs the client Daemon on the host's machine (IN PROD)

    """
    try:
        print(stylize("Launching the Vectordash client on this machine", fg("green")))
        print("Currently in production...")

        # TODO
        # This command should invoke the client Daemon

    except ValueError as e:
        print(stylize("The following error was thrown: ", fg("red")) + str(e))
        print(stylize("Your mining commands could not be executed. Are you sure you are using absolute paths?",
                      fg("red")))
