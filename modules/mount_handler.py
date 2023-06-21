## Main file, this file will be responsible for handling the commands
import os
import subprocess
import sys


def check_mount():
    cmd = subprocess.run(["findmnt", "-f", "/mnt"], capture_output=False, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    if cmd.returncode != 0:
        sys.exit("There is no drive mounted on '/mnt'. Please mount")
    else:
        print("Found /mnt")

def mount(device):
    cmd = subprocess.run(["mount", device, "/mnt"])
    if cmd.returncode != 0:
        sys.exit(cmd.stderr)