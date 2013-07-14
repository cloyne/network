#!/usr/bin/env python

import sys
import argparse

from command import cmd

# handle args
parser = argparse.ArgumentParser(description="import router config")
parser.add_argument('configs', metavar='F', type=str, nargs='+',
                    help='a config file to import')
args = parser.parse_args()

# get config
config = []
for file_name in args.configs:
  with open(file_name, 'r') as file:
    config.extend(file.readlines())

print "config", config

# parse config
def parseConfig(config):
  command = None
  for line in config:
    if line.startswith('/'):
      if command:
        yield "".join(command)
      command = []
    command.extend(line)
  yield "".join(command)

# send config over ssh
for command in parseConfig(config):
  print "Asfd"
  print command
  cmd(command)
