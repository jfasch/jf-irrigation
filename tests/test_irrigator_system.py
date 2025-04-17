from core.irrigator import Irrigator
from core.irrigator_system import IrrigatorSystem
from core.moisture_mock import MockMoistureSensor
from core.switch_mock import MockSwitch
from core.hysteresis import Hysteresis


def test_basic():
    irrigator_tomatoes = Irrigator(
        name = 'tomatoes',
        sensor = MockMoistureSensor(value=10),
        switch = MockSwitch(state=False),
        low = 30,
        high = 40,
    )
    irrigator_beans = Irrigator(
        name = 'beans',
        sensor = MockMoistureSensor(value=20),
        switch = MockSwitch(state=False),
        low = 10,
        high = 20,
    )
    irrigator_system = IrrigatorSystem((irrigator_tomatoes, irrigator_beans))

    irrigator_system.check()
    assert irrigator_tomatoes.switch.get_state() == True
    assert irrigator_beans.switch.get_state() == False

    irrigator_beans.sensor.set_value(5)
    irrigator_system.check()
    assert irrigator_tomatoes.switch.get_state() == True
    assert irrigator_beans.switch.get_state() == True

    irrigator_tomatoes.sensor.set_value(45)
    irrigator_beans.sensor.set_value(25)
    irrigator_system.check()
    assert irrigator_tomatoes.switch.get_state() == False
    assert irrigator_beans.switch.get_state() == False

def test_need_water():
    irrigator_tomatoes = Irrigator(
        name = 'tomatoes',
        sensor = MockMoistureSensor(value=10),
        switch = MockSwitch(state=False),
        low=30, 
        high=40, 
    )
    irrigator_beans = Irrigator(
        name = 'beans',
        sensor = MockMoistureSensor(value=20),
        switch = MockSwitch(state=False),
        low=10, 
        high=20, 
    )
    irrigator_system = IrrigatorSystem((irrigator_tomatoes, irrigator_beans))

    irrigator_system.check()
    assert irrigator_system.needs_water == True

    irrigator_system.check()
    assert irrigator_system.needs_water == True
    
    irrigator_tomatoes.sensor.set_value(35)

    irrigator_system.check()
    assert irrigator_system.needs_water == True

def test_public_iface_for_dbus():
    irrigator_tomatoes = Irrigator(
        name = 'tomatoes',
        sensor = MockMoistureSensor(value=10),
        switch = MockSwitch(state=False),
        low = 30,
        high = 40,
    )
    irrigator_beans = Irrigator(
        name = 'beans',
        sensor = MockMoistureSensor(value=20),
        switch = MockSwitch(state=False),
        low = 10,
        high = 20,
    )
    irrigator_system = IrrigatorSystem((irrigator_tomatoes, irrigator_beans))

    assert irrigator_system.get_irrigator('tomatoes') is irrigator_tomatoes
    assert irrigator_system.get_irrigator('beans') is irrigator_beans
    irrigator_system.check()
    assert irrigator_system.needs_water
