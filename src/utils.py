import platform

from termcolor import colored

OS = platform.system()
ERR = colored(f"Not implemented for OS \"{OS}\".", "red")


def get_package_installer_command():
    if OS == "Darwin":
        return "brew install --cask"
    elif OS == "Linux":
        return "pacman -S"
    else:
        raise Exception(ERR)


def get_package_uninstaller_command():
    if OS == "Darwin":
        return "brew uninstall --cask"
    elif OS == "Linux":
        return "pacman -R"
    else:
        raise Exception(ERR)
