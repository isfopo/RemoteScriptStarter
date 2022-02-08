'''
  This script is designed to help with debugging by dynamically displaying
  the contents of the log file that Ableton creates when running. This
  should help find and solve errors and get feedback from your script
  the same way a console would.

  This script also takes a guess at your username for the path. If this guess
  is incorrect or there is some kind of error, try adding your username with
  the `--user` flag.
'''

import os
import getpass
import argparse
import platform

from watcher import Watcher

LOGPATHWIN = """C:\\Users\\{user}\\AppData\\Roaming\\Ableton\\Live 11.0.12\\Preferences\\Log.txt"""

LOGPATHMAC = """
Macintosh HD/Users/{user}/Library/Preferences/Ableton/Live x.x.x/Log.txt
"""

parser = argparse.ArgumentParser(description='Install remote script')
parser.add_argument('--user', '-your account username', required=False)

args = parser.parse_args()

user = args.user or getpass.getuser()

# need to deal with getting the lastest version number

logPath = (
    LOGPATHWIN if platform.system() == 'Windows' else LOGPATHMAC
).format(user=user)


def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def onChange(filename):
    clear()
    with open(filename, encoding='utf-8') as file:
        for line in (file.readlines()[-100:]):
            print(line, end='')


watcher = Watcher(logPath, onChange)
watcher.watch()
