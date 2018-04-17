import click
import subprocess
import os

from colored import fg
from colored import stylize


@click.command(name='start-miner')
def start_miner():
    """
    args: None |
    Run the miner on the machine that was set up by user

    """
    try:
        # Path to mining bash file
        mining_path = os.path.expanduser('~/.vectordash/mining/mine.sh')

        # Path to mining pid file
        pid_path = os.path.expanduser('~/.vectordash/mining/pid')

        # If the mining file has been created, run the miner
        if os.path.exists(mining_path):
            print("Running the miner...")
            args = ['chmod', '+x', mining_path]
            subprocess.check_call(args)
            p = subprocess.Popen(mining_path)

            # write pid to file
            f = open(pid_path, 'w')
            f.write(str(p.pid))
            f.close()

        else:
            print("Please run " + stylize("vdhost set-commands", fg("blue")) + " before trying to mine.")

    except Exception as e:
        print(stylize("The following error was encountered: ", fg("red")) + str(e))
        print(stylize("Your mining commands could not be executed. Are you sure you are using absolute paths?",
                      fg("red")))

