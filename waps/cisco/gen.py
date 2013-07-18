#!/usr/bin/env python

import argparse

import pystache

# get user input
parser = argparse.ArgumentParser(description="generates Cisco Aironet 1140 Series Access Point configs")
parser.add_argument('hostname',
                    help='in format <LOCATION>-<TYPE>-<MODIFIER>')
parser.add_argument('ip_address',
                    help='in format 192.168.0.x')

args = parser.parse_args()

# get template
with open("wap.cisco", 'r') as f:
  template = f.read()

# embed user input in template
config = pystache.render(template, args)

# save config
configPath = "../../network/%s.cisco" % args.hostname
with open(configPath, 'w+') as f:
  f.write(config)
  print "wrote to %s" % configPath

# TODO add wap to network.csv
