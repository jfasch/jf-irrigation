#!/usr/bin/env python

from irrigation.dbus.interfaces import DBusIrrigationSystem, DBusIrrigator

import asyncio


irrigation_system = DBusIrrigationSystem.new_proxy('me.faschingbauer.IrrigationService', '/me/faschingbauer/IrrigationSystem')
irrigators = []

async def setup():
    irrigator_names = await irrigation_system.GetIrrigatorNames()
    for name in irrigator_names:
        irrigator = DBusIrrigator.new_proxy('me.faschingbauer.IrrigationService', f'/me/faschingbauer/IrrigationSystem/{name}')
        await irrigator.Name
        irrigators.append(irrigator)

async def status_loop():
    while True:
        for irrigator in irrigators:
            name = await irrigator.Name
            low = await irrigator.Low
            high = await irrigator.High
            moisture = await irrigator.MoistureValue
            switch_state = await irrigator.SwitchState

            print(name, low, high, moisture, switch_state)

        await asyncio.sleep(2)

async def consume_signals():
    async for switches_changed in irrigation_system.SwitchStateChanged:
        print('SWITCHES CHANGED:', switches_changed)

async def main():
    await setup()

    async with asyncio.TaskGroup() as tg:
        tg.create_task(status_loop())
        tg.create_task(consume_signals())

asyncio.run(main())
