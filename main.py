from modules import mount_handler, qcow2_handler
import argparse
import os
import subprocess
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--mount', '-m', help="Should OS-Deployer mount a device for you?", action='store_true')
    parser.add_argument('--device', '-d', nargs=1, help="Positional argument")
    parser.add_argument('--qcow2', '-q', nargs=1, help="QCOW2 file to deploy")
    return parser

def root_check():
  if not 'SUDO_UID' in os.environ.keys() or os.geteuid() != 0:
    sys.exit("OS-Deployer needs sudo or root")

def main(args, parser):
  root_check()
  qcow2_handler.qemu_dd(args.qcow2, args.device)
  if args.mount:
      if not args.device:
          print("Error: Positional argument is required when using the --mount option.")
          return
      check_mount(args.device)
  else:
      parser.print_help()

if __name__ == "__main__":
  parser = parse_arguments()
  args = parser.parse_args()
  main(args, parser)