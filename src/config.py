import os
import sys

PATH_TO_THIS_FILE = sys.argv[0]
PATH_TO_THIS_DIR = os.path.dirname(PATH_TO_THIS_FILE)

URL_TO_DOOM = "https://github.com/doomemacs/doomemacs"
URL_TO_DOOM_CONF = "https://github.com/vincentmader/doom-emacs-conf"

PATH_TO_EMACS_DIR = "~/.emacs.d"

PATH_TO_DOOM_DIR = "~/.doom.d"
PATH_TO_DOOM_BINARY = os.path.join(PATH_TO_EMACS_DIR, "bin", "doom")

PATH_TO_THEME_SETUP_BINARY = os.path.join(
    PATH_TO_DOOM_DIR, "bin", "setup_custom_theme.py"
)

EMACS_BINARY_VERSION = "homebrew-cask"
# EMACS_BINARY_VERSION = "homebrew-emacsmacport"
