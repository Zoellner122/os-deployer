from modules import *
import argparse
import os
import subprocess
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--mount', '-m', help="Should OS-Deployer mount a device for you?", action='store_true')
    parser.add_argument('device', nargs='?', help="Positional argument")
    return parser

def root_check():
  if not 'SUDO_UID' in os.environ.keys()or os.geteuid() != 0:
    sys.exit("OS-Deployer requires super-user or root")
 
def main(args, parser):
    if args.mount:
        if not args.device:
            print("Error: Positional argument is required when using the --mount option.")
            return
        mount(args.device)
    else:
        parser.print_help()

if __name__ == "__main__":
  parser = parse_arguments()
  args = parser.parse_args()
  root_check()
  main(args, parser)