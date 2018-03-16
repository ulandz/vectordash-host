import click

from colored import fg
from colored import stylize
from colored import attr


@click.command()
def setcommands():
    """
    args: None
    Prompt user to set up commands for mining on their machine

    """
    try:
        commands = []

        # get commands from user
        cmd = input(
            "Please enter the commands you use to start your miner, line by line. Once you are done, do not type anything and press Enter twice:\n\n")
        commands.append(cmd)

        while (1):
            cmd = input("")
            if (cmd == ''):
                break
            commands.append(cmd)

        f = open('/mining/mine.sh', 'w')
        f.write("#!/usr/bin/env bash\n")
        for cmd in commands:
            f.write(cmd)
            f.write('\n')
        f.close()

        f = open('pid.txt', 'w')
        f.write('-1')
        f.close()

    except TypeError:
        type_err = "There was an error in your provided commands. Please try again. "
        # print(type_err + stylize("vectordash secret <token>", fg("blue")))


if __name__ == "__main__":
    setcommands()
