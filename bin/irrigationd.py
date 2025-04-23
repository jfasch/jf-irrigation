#!/usr/bin/env python3

from irrigation.core.config import Config
from irrigation.dbus.interfaces import DBusIrrigationSystem, DBusIrrigator

import argparse
import sdbus
import asyncio


parser = argparse.ArgumentParser(description='Irrigation system (D-Bus daemon).')
parser.add_argument('--configfile', required=True)
args = parser.parse_args()

irrigation_system_local = Config(args.configfile).instantiate()
        
async def main():
    # setup
    await sdbus.request_default_bus_name_async('me.faschingbauer.IrrigationService')

    irrigation_system_dbus = DBusIrrigationSystem(irrigation_system_local)
    irrigation_system_dbus.export_to_dbus('/me/faschingbauer/IrrigationSystem')

    irrigators_dbus = {}
    for name, irrigator in irrigation_system_local.irrigators.items():
        irrigator_dbus = DBusIrrigator(irrigator)
        irrigator_dbus.export_to_dbus(f'/me/faschingbauer/IrrigationSystem/{name}')
        irrigators_dbus[name] = irrigator_dbus

    # check every <interval> seconds, and emit switch-changed signals
    while True:
        switches_changed = irrigation_system_local.check()
        if len(switches_changed) != 0:
            irrigation_system_dbus.SwitchStateChanged.emit(switches_changed)
        await asyncio.sleep(1)

asyncio.run(main())
