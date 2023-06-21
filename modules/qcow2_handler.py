# This module will handle the qcow files #
import os
import subprocess
import sys

def qemu_dd(filename, device):
  path = str(filename[0])
  print(path)
  if not path.isfile():
    sys.exit("Filepath is incorrect")
  else:
    command = subprocess.run(["qemu-img", "convert", filename, "-O", "raw", device], shell=True, capture_output=True)
    if command.returncode != 0:
      print(command.stderr)
    
    
    