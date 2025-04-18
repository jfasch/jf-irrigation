#!/usr/bin/env python3

from core.config import Config
from dbus.export import export_system

import asyncio
import argparse


parser = argparse.ArgumentParser(description='Irrigation system (D-Bus daemon).')
parser.add_argument('--configfile', required=True)
args = parser.parse_args()

irrigation_system = Config(args.configfile).instantiate()
        
async def main():
    await export_system(irrigation_system)
    while True:
        irrigation_system.check()
        await asyncio.sleep(1)

asyncio.run(main())
