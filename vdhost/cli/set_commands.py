import click
import os
from colored import fg
from colored import stylize
import json


@click.command(name='set-commands')
@click.argument('gpu_id', nargs=1, type=int)
def set_commands(gpu_id):
    """
    args: gpu_id |
    Prompt user to set up commands for mining on their machine

    """
    try:
        # Path to mining directory
        dot_folder = os.path.expanduser('~/.vectordash/')
        mining_folder = os.path.expanduser(dot_folder + 'mining/')
        commands_file = mining_folder + 'commands'
        pid_file = mining_folder + 'pid'

        curr_data = {} # dict containing current data

        # If the .vectordash directory doesn't exist, create both it and the mining directory
        if not os.path.isdir(dot_folder):
            os.mkdir(dot_folder)
            os.mkdir(mining_folder)
            f = open(commands_file, 'w+')
            f.write('{}')
            f.close()
            f = open(pid_file, 'w+')
            f.write('{}')
            f.close()

        # If the mining directory doesn't exist, create it
        elif not os.path.isdir(mining_folder):
            os.mkdir(mining_folder)
            f = open(commands_file, 'w+')
            f.write('{}')
            f.close()
            f = open(pid_file, 'w+')
            f.write('{}')
            f.close()


        # read from commands file
        f = open(commands_file, 'r')
        dat = f.read()
        f.close()

        curr_data = json.loads(dat) # dict
        

        # Mining commands list
        #commands = []

        # get commands from user
        #cmd = input(stylize("Please enter the commands you use to start your miner, line by line.\n"
        #                    "Make sure that all paths provided are absolute paths\n"
        #            "Once you are done, do not type anything and press ENTER twice:\n\n", fg("green")))
        
        cmd = input(stylize("Please enter the path to a bash script that, when run, will start mining " + 
                "on the GPU with id " + str(gpu_id) + ":\n\n", fg("green")))
        curr_data[gpu_id] = cmd
        
        new_data = json.dumps(curr_data) # string

        # write back to commands file
        f = open(commands_file, 'w')
        f.write(new_data)
        f.close()

        # read from pid file
        f = open(pid_file, 'r')
        dat = f.read()
        f.close()

        curr_pid = json.loads(dat) # dict
        curr_pid[gpu_id] = -1
        new_pid = json.dumps(curr_pid) # string
        
        # write back to pid file
        f = open(pid_file, 'w')
        f.write(new_pid)
        f.close()

        #commands.append(cmd)

        # Add all of the input commands to the list
        #while 1:
        #    cmd = input("")
        #    if cmd == '':
        #        break
        #    commands.append(cmd)

        # Save commands to mining bash file
        #mine_file = mining_folder + 'mine.sh'
        #f = open(mine_file, 'w')
        #f.write("#!/usr/bin/env bash\n")
        #for cmd in commands:
        #    f.write(cmd)
        #    f.write('\n')
        #f.close()

        # Mining process is NOT running, so give pid file a value of -1
        #f = open(pid_file, 'w+')
        #f.write('-1')
        #f.close()

    except Exception as e:
        print(stylize("The following error was encountered: ", fg("red")) + str(e))
