import click
import subprocess
import os
import json

from colored import fg
from colored import stylize


@click.command(name='start-miner')
@click.argument('gpu_id', nargs=1, type=int)
def start_miner(gpu_id):
    """
    args: gpu_id |
    Run the miner on the machine that was set up by user with vdhost set-commands

    """
    try:
        # Path to mining bash file
        var_folder = os.path.expanduser('/var/')
        var_vd_folder = os.path.expanduser(var_folder + 'vectordash/')
        mining_folder = os.path.expanduser(var_vd_folder + 'mining/')
        commands_file = os.path.expanduser(mining_folder + 'commands')

        # Path to mining pid file
        #pid_file = os.path.expanduser('~/.vectordash/mining/pid')

        if not os.path.isfile(var_vd_folder + 'install_complete'):
            print(stylize("Please run 'vdhost install' first!", fg("red")))
            return

        # If the mining file has been created, run the miner
        if os.path.exists(commands_file):
            # read commands file
            f = open(commands_file, 'r')
            commands = f.read()
            f.close()
            
            # turn commands str into dict
            commands = json.loads(commands)
            print(commands)
            # get command associated with gpu_id and run miner if possible
            if str(gpu_id) in commands.keys():
                # run the miner
                cmd = commands[str(gpu_id)]
                print("Running the miner...")
                args = ['chmod', '+x', cmd]
                subprocess.check_call(args)
                p = subprocess.Popen(cmd.split(' '), preexec_fn=os.setsid)                

                # read pid file
                #f = open(pid_file, 'r')
                #pid_dat = f.read()
                #f.close()

                # convert to dict
                #pid_dat = json.loads(pid_dat)
                # update
                #pid_dat[gpu_id] = p.pid
                #pid_dat.update({str(gpu_id): p.pid})

                # write pid file
                #f = open(pid_file, 'w')
                #f.write(json.dumps(pid_dat))
                #f.close()

            else:
                print("Please run " + stylize("vdhost set-commands " + str(gpu_id), fg("blue")) 
                        + " before trying to mine.")

        else:
            print("Please run " + stylize("vdhost set-commands " + str(gpu_id), fg("blue")) 
                        + " before trying to mine.")

    except Exception as e:
        print(stylize("The following error was encountered: ", fg("red")) + str(e))
        print(stylize("Your mining commands could not be executed. Are you sure you are using absolute paths?",
                      fg("red")))

