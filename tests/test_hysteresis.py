from irrigation.core.hysteresis import Hysteresis
from irrigation.core.sensor_mock import MockSensor
from irrigation.core.switch_mock import MockSwitch


def test_basic():
    sensor = MockSensor(value=25)
    switch = MockSwitch(state=False)
    hyst = Hysteresis(low=20.0, high=30.0, sensor=sensor, switch=switch)

    hyst.check()
    assert switch.get_state() == False

    sensor.set_value(20)
    hyst.check()
    assert switch.get_state() == False

    sensor.set_value(19)
    hyst.check()
    assert switch.get_state() == True

    sensor.set_value(30)
    hyst.check()
    assert switch.get_state() == True

    sensor.set_value(31)
    hyst.check()
    assert switch.get_state() == False
