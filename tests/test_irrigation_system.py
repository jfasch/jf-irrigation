from irrigation.irrigator import Irrigator
from irrigation.irrigation_system import IrrigationSystem
from irrigation.sensor_mock import MockSensor
from irrigation.switch_mock import MockSwitch
from irrigation.hysteresis import Hysteresis


def test_basic():
    irrigator_tomatoes = Irrigator(
        name = 'tomatoes',
        sensor = MockSensor(value=10),
        switch = MockSwitch(state=False),
        low = 30,
        high = 40,
    )
    irrigator_beans = Irrigator(
        name = 'beans',
        sensor = MockSensor(value=20),
        switch = MockSwitch(state=False),
        low = 10,
        high = 20,
    )
    irrigation_system = IrrigationSystem((irrigator_tomatoes, irrigator_beans))

    irrigation_system.check()
    assert irrigator_tomatoes.switch.get_state() == True
    assert irrigator_beans.switch.get_state() == False

    irrigator_beans.sensor.set_value(5)
    irrigation_system.check()
    assert irrigator_tomatoes.switch.get_state() == True
    assert irrigator_beans.switch.get_state() == True

    irrigator_tomatoes.sensor.set_value(45)
    irrigator_beans.sensor.set_value(25)
    irrigation_system.check()
    assert irrigator_tomatoes.switch.get_state() == False
    assert irrigator_beans.switch.get_state() == False

def test_switches_changed():
    irrigator_tomatoes = Irrigator(
        name = 'tomatoes',
        sensor = MockSensor(value=10),
        switch = MockSwitch(state=False),
        low = 30,
        high = 40,
    )
    irrigator_beans = Irrigator(
        name = 'beans',
        sensor = MockSensor(value=15),
        switch = MockSwitch(state=False),
        low=10, 
        high=20, 
    )
    irrigation_system = IrrigationSystem((irrigator_tomatoes, irrigator_beans))

    switches_changed = irrigation_system.check()
    assert len(switches_changed) == 1
    assert switches_changed['tomatoes'] == True

    switches_changed = irrigation_system.check()
    assert len(switches_changed) == 0

    irrigator_tomatoes.sensor.set_value(45)    # above high -> off
    switches_changed = irrigation_system.check()
    assert len(switches_changed) == 1
    assert switches_changed['tomatoes'] == False

    switches_changed = irrigation_system.check()
    assert len(switches_changed) == 0

    irrigator_tomatoes.sensor.set_value(0)
    irrigator_beans.sensor.set_value(0)
    switches_changed = irrigation_system.check()
    assert len(switches_changed) == 2
    assert switches_changed['tomatoes'] == True
    assert switches_changed['beans'] == True
