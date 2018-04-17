import click
import os
from colored import fg
from colored import stylize


@click.command(name='set-gpu-ids')
@click.argument('gpu_ids', required=True, nargs=-1)
def set_gpu_ids(gpu_ids):
    """
    args: IDs |
    Allow user to select the GPUs they would like to rent out on Vectordash

    """
    try:
        # Path to .vectordash directory
        dot_folder = os.path.expanduser('~/.vectordash/')

        # If the .vectordash directory doesn't exist, create it
        if not os.path.isdir(dot_folder):
            os.mkdir(dot_folder)

        # Path to gpu_ids file
        gpu_ids_file = dot_folder + 'gpu_ids'

        # Parse gpu ids
        temp = str(gpu_ids)
        temp1 = temp.replace('(', '')
        temp2 = temp1.replace(')', '')
        temp3 = temp2.replace(',', '')
        final_ids = temp3.replace('\'', '')

        # Write the ids to the file
        f = open(gpu_ids_file, 'w')
        f.write(str(final_ids))
        f.close()

        print(stylize("Saved GPU IDs", fg("green")))
        print("If you have already ran " + stylize("vdhost install", fg("blue")) +
              " successfully, you can now list your machine on Vectordash by running " +
              stylize("vdhost launch", fg("blue")))

    except Exception as e:
        print(stylize("The following error was encountered: ", fg("red")) + str(e))
