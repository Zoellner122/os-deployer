# This module is responsible to check if a drive is mounted and if not mount it #
import os
import subprocess
import sys

def check_mount():
    cmd = subprocess.run(["findmnt", "-f", "/mnt"], capture_output=False, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    if cmd.returncode != 0:
        mount(device)
    else:
        print("Found /mnt")

def mount(device):
    cmd = subprocess.run(["mount", device, "/mnt"])
    if cmd.returncode != 0:
        sys.exit(cmd.stderr)