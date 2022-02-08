'''
  This script is designed to help with debugging by dynamically displaying
  the contents of the log file that Ableton creates when running. This
  should help find and solve errors and get feedback from your script
  the same way a console would.

  This script also takes a guess at your username for the path. If this guess
  is incorrect or there is some kind of error, try adding your username with
  the `--user` flag.

  This script assumes you are using the lastest version of Live that is
  installed on your machine. If you are not or this script is throwing errors,
  use the `--version` flag to specific your version. Example: "Live 11.0.12"
'''

import os
import re
import getpass
import argparse
import platform

from watcher import Watcher

ABLETONPATHWIN = "C:\\Users\\{user}\\AppData\\Roaming\\Ableton\\"

ABLETONPATHMAC = "Macintosh HD/Users/{user}/Library/Preferences/Ableton/"

LOGPATHWIN = "Preferences\\Log.txt"

LOGPATHMAC = "Log.txt"

parser = argparse.ArgumentParser(description='Install remote script')
parser.add_argument('--user', '-your account username', required=False)
parser.add_argument('--version', '-your version of Live', required=False)

args = parser.parse_args()

user = args.user or getpass.getuser()


abletonPath = (
    ABLETONPATHWIN if platform.system() == 'Windows' else ABLETONPATHMAC
).format(user=user)


def getVersionKey(version):
    search = re.search('(\\d+)\\.(\\d+)\\.(\\d+)', version)
    if search:
        major, minor, bug = search.groups()
        return int(major), int(minor), int(bug)


version = args.version or max(
    filter(
        lambda name: not name == "Live Reports", os.listdir(abletonPath)
    ), key=getVersionKey
)

logPath = os.path.join(
    abletonPath,
    version,
    LOGPATHWIN if platform.system() == 'Windows' else LOGPATHMAC
)


def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def onChange(filename):
    clear()
    with open(filename, encoding='utf-8') as file:
        for line in (file.readlines()[-100:]):
            print(line, end='')


watcher = Watcher(logPath, onChange)
watcher.watch()
