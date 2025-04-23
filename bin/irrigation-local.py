#!/usr/bin/env python3

from irrigation.core.config import Config

import time
import argparse


parser = argparse.ArgumentParser(description='Irrigation system (only local, no D-Bus).')
parser.add_argument('--configfile', required=True)
args = parser.parse_args()

irrigation_system = Config(args.configfile).instantiate()

while True:
    irrigation_system.check()
    time.sleep(1)
