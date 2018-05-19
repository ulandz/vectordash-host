import click
import subprocess
import os

from colored import fg
from colored import stylize


@click.command(name='stop-miner')
@click.argument('gpu_id', nargs=1, type=int)
def stop_miner(gpu_id):
    """
    args: gpu_id |
    Stop the mining process on the host's machine

    """
    try:
        # Path to the mining pid file
        pid_file = os.path.expanduser('~/.vectordash/mining/pid')

        # If the mining pid file exists, stop the miner
        
        if not os.path.exists(pid_file):
            print("Please run " + stylize("vdhost start_miner " + str(gpu_id), 
                fg("blue")) + " before trying to stop mining.")
            return

        # read pid file
        f = open(pid_file, 'r')
        pid_dat = f.read()
        f.close()
        
        # convert to dict
        pid_dat = json.loads(pid_dat)
        pid = pid_dat[gpu_id]

        # If the pid file has nonnegative pid, stop the miner
        if pid is not None:

            # Read in pid (number)
            #print("Stopping the mining process now...")
            #f = open(pid_path, 'r')
            #p = f.read()
            #f.close()

            # If the pid is below 0, then it is currently not running
            if pid < 0:
                print("Not currently mining. Run " + stylize("vdhost start_miner " + str(gpu_id), 
                    fg("blue")) + " to start mining")
                return

            print("Stopping the mining process now...")

            # kill the process with process id pid
            args = ['kill', '--', '-$(ps', '-o', 'pgid=', str(pid), '|', 'grep', '-o', '[0-9]*)']
            subprocess.check_call(args)

            # If the pids have not yet been killed, try again
            while pid_exists(str(pid)):
                print("Attempting to stop mining")
                args2 = ['kill', '-9', '-p', str(pid)]
                subprocess.check_call(args2)

            # update dict
            pid_dat[gpu_id] = -1

            # write to pid file
            f = open(pid_file, 'w')
            f.write(json.dumps(pid_dat))
            f.close()

        else:
            print("Please run " + stylize("vdhost start_miner " + str(gpu_id), 
                fg("blue")) + " before trying to stop mining.")
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

