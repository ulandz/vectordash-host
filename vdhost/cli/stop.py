import click
import subprocess
import os

from colored import fg
from colored import stylize
from colored import attr


@click.command()
def stop():
    """
    args: None
    Prompt user to set up commands for mining on their machine

    """
    try:
        if (not os.path.exists("pid")):
            print("Please run the Vectordash client before trying to stop mining.")
            return
       
        f = open("pid", 'r')
        p = f.read()
        f.close()

        if (int(p) < 0):    
            return
        
        # kill the process with process id pid
        subprocess.call("kill " + p)

        # write -1 to pid file
        f = open("pid", 'w')
        f.write("-1")
        f.close()
  
    except TypeError:
        type_err = "There was an error in your provided commands. Please try again. "
        # print(type_err + stylize("vectordash secret <token>", fg("blue")))


if __name__ == "__main__":
    stop()
