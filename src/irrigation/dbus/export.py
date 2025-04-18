from .interfaces import DBusIrrigationSystem, DBusIrrigator

import sdbus


_dbus_objects = []      # ensure that we keep them referenced

async def export_system(irrigation_system):
    await sdbus.request_default_bus_name_async('me.faschingbauer.IrrigationService')

    dbus_irrigation_system = DBusIrrigationSystem(irrigation_system)
    _dbus_objects.append(dbus_irrigation_system)
    dbus_irrigation_system.export_to_dbus('/me/faschingbauer/IrrigationSystem')

    for name, irrigator in irrigation_system.irrigators.items():
        dbus_irrigator = DBusIrrigator(irrigator)
        _dbus_objects.append(dbus_irrigator)
        dbus_irrigator.export_to_dbus(f'/me/faschingbauer/IrrigationSystem/{name}')
