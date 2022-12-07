#!/usr/bin/env python3
import subprocess

import config as cfg
import utils


def install_emacs_vanilla():
    # TODO Think re: Use Emacs-Mac instead?
    #   -> https://github.com/railwaycat/homebrew-emacsmacport
    install = utils.get_package_installer_command()
    cmd = f"{install} emacs"
    exit_code = subprocess.Popen(cmd, shell=True).wait()
    return exit_code


def install_emacs_doom():
    doom_url = cfg.URL_TO_DOOM
    emacs_dir = cfg.PATH_TO_EMACS_DIR
    doom_dir = cfg.PATH_TO_DOOM_DIR
    conf_url = cfg.URL_TO_DOOM_CONF
    doom = cfg.PATH_TO_DOOM_BINARY

    cmds = [
        f"git clone --depth 1 {doom_url} {emacs_dir}",
        f"git clone {conf_url} {doom_dir}",
        f"{doom} install",
    ]
    for cmd in cmds:
        exit_code = subprocess.Popen(cmd, shell=True).wait()
        if exit_code:
            return exit_code
    return 0


def setup_emacs_doom():
    theme_setup = cfg.PATH_TO_THEME_SETUP_BINARY
    doom = cfg.PATH_TO_DOOM_BINARY

    cmds = [
        theme_setup,
        f"{doom} sync"
    ]
    for cmd in cmds:
        exit_code = subprocess.Popen(cmd, shell=True).wait()
        if exit_code:
            return exit_code


if __name__ == "__main__":
    tasks = [
        install_emacs_vanilla,
        install_emacs_doom,
        setup_emacs_doom,
    ]
    for task in tasks:
        if task():
            break
