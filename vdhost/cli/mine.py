import click
import subprocess
import os

from colored import fg
from colored import stylize
from colored import attr


@click.command()
def mine():
    """
    args: None
    Prompt user to set up commands for mining on their machine

    """
    try:
        if (not os.path.exists("mine.sh")):
            print("Please run 'vdhost set-commands' before trying to mine.")
        p = subprocess.Popen("./mine.sh")
        
        # write pid to file
        f = open("pid", 'w')
        f.write(str(p.pid))
        f.close()
  
    except TypeError:
        type_err = "There was an error in your provided commands. Please try again. "
        # print(type_err + stylize("vectordash secret <token>", fg("blue")))


if __name__ == "__main__":
    mine()
