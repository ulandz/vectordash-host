import subprocess
import os


commands = list()

def get_commands():
    global commands

    # get commands from user 
    cmd = input("Please enter the commands you use to start your miner, line by line. Once you are done, do not type anything and press Enter twice:\n\n")
    commands.append(cmd)
 
    while(1):
        cmd = input("") 
        if (cmd == ''):
            break
        commands.append(cmd)

    f = open('mine.sh', 'w')
    f.write("#!/usr/bin/env bash\n")
    for cmd in commands:
        f.write(cmd)
        f.write('\n')
    f.close()

    f = open('pid.txt', 'w')
    f.write('-1')
    f.close()

def mine():

    if (len(commands) == 0 and (not os.path.isfile("mine.sh"))):
        print("No mining commands set.")
        return

    rc = subprocess.call("./mine.sh")
        
if __name__ == "__main__":
    get_commands()
    mine() 
