import click
import subprocess
import os

from colored import fg, attr, stylize


@click.command(name='status')
def status():
    """
    Checks the status of the Vectordash client.
    """
    try:

        # note that supervisor prints a message, so we don't need to print one ourselves
        subprocess.call("sudo supervisorctl status vdclient", shell=True)

    except OSError:
        print(stylize("Please run as sudo: ", fg("red")) + stylize("sudo vdhost status", fg("blue")))

