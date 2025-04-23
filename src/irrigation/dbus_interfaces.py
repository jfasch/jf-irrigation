from sdbus import DbusInterfaceCommonAsync, dbus_method_async, dbus_property_async, dbus_signal_async


class DBusIrrigationSystem(
        DbusInterfaceCommonAsync,
        interface_name='me.faschingbauer.IrrigationSystem'
):
    def __init__(self, irrigation_system):
        super().__init__()
        self.irrigation_system = irrigation_system

    @dbus_method_async(result_signature='as')
    async def GetIrrigatorNames(self) -> list[str]:
        return self.irrigation_system.get_irrigator_names()

    @dbus_signal_async(
        signal_signature='a{sb}'
    )
    def SwitchStateChanged(self):
        raise NotImplementedError

class DBusIrrigator(
        DbusInterfaceCommonAsync,
        interface_name='me.faschingbauer.Irrigator'
):
    def __init__(self, irrigator):
        super().__init__()
        self.irrigator = irrigator

    @dbus_property_async(property_signature='s')
    def Name(self):
        return self.irrigator.name

    @dbus_property_async(property_signature='d')
    def Low(self):
        return float(self.irrigator.low)

    @dbus_property_async(property_signature='d')
    def High(self):
        return float(self.irrigator.high)

    @dbus_property_async(property_signature='d')
    def MoistureValue(self):
        return float(self.irrigator.sensor.get_value())

    @dbus_property_async(property_signature='b')
    def SwitchState(self):
        return self.irrigator.switch.get_state()

