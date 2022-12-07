#!/usr/bin/env python3
import subprocess
from termcolor import colored

from config import PATH_TO_DOOM_DIR as DOOM_DIR
from config import PATH_TO_EMACS_DIR as EMACS_DIR
import utils


WARNING = f"WARNING:\
    \nMake sure not to delete unsaved changes to the `{DOOM_DIR}` repo!\
    \n(Press `Enter` to continue.)"


def uninstall_emacs():
    uninstall = utils.get_package_uninstaller_command()

    cmd = f"{uninstall} emacs"
    _ = subprocess.Popen(cmd, shell=True).wait()


def remove_emacs_directories():
    input(colored(WARNING, "yellow"))

    cmds = [
        f"sudo rm -r {EMACS_DIR} 2> /dev/null",
        f"sudo rm -r {DOOM_DIR} 2> /dev/null",
    ]
    for cmd in cmds:
        _ = subprocess.Popen(cmd, shell=True).wait()


if __name__ == "__main__":
    uninstall_emacs()
    remove_emacs_directories()
