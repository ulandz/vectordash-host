import click
import subprocess
import os

from colored import fg
from colored import stylize


@click.command(name='stop-miner')
def stop_miner():
    """
    args: None |
    Stop the mining process on the host's machine

    """
    try:
        # Path to the mining pid file
        pid_path = os.path.expanduser('~/.vectordash/mining/pid')

        # If the mining pid file exists, stop the miner
        if os.path.exists(pid_path):

            # Read in pid (number)
            print("Stopping the mining process now...")
            f = open(pid_path, 'r')
            p = f.read()
            f.close()

            # If the pid is below 0, then it is currently not running
            if int(p) < 0:
                print("Not currently mining. Run " + stylize("vdhost mine", fg("blue")) + " to start mining")
                return

            # kill the process with process id pid
            args = ['kill', '--', '-$(ps', '-o', 'pgid=', p, '|', 'grep', '-o', '[0-9]*)']
            subprocess.check_call(args)

            # If the pids have not yet been killed, try again
            while pid_exists(p):
                print("Attempting to stop mining")
                args2 = ['kill', '-9', '-p', p]
                subprocess.check_call(args2)

            # write -1 to pid file (indicating the mining has stopped)
            f = open(pid_path, 'w')
            f.write("-1")
            f.close()

        else:
            print("Please run " + stylize("vdhost mine", fg("blue")) + " before trying to stop mining.")
            return
  
    except ValueError as e:
        print(stylize("The following error was encountered: ", fg("red")) + str(e))
        print(stylize("Your miner could not be stopped. Are you sure you are using absolute paths?", fg("red")))


def pid_exists(pid):
    """
    Check whether pid exists in the current process table.
    """
    try:
        print("Double-checking to ensure mining was stopped")
        os.kill(int(pid), 0)
    except OSError:
        print("Pid: " + pid + " killed")
        return False
    else:
        print("Pid: " + pid + " still exists")
        return True

