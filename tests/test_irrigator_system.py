from core.irrigator_system import IrrigatorSystem
from core.moisture_mock import MockMoistureSensor
from core.switch_mock import MockSwitch
from core.hysteresis import Hysteresis


def test_basic():
    sensor_tomatoes = MockMoistureSensor(value=10)
    switch_tomatoes = MockSwitch(state=False)
    hyst_tomatoes = Hysteresis(low=30, high=40, sensor=sensor_tomatoes, switch=switch_tomatoes)

    sensor_beans = MockMoistureSensor(value=20)
    switch_beans = MockSwitch(state=False)
    hyst_beans = Hysteresis(low=10, high=20, sensor=sensor_beans, switch=switch_beans)

    irrigator_system = IrrigatorSystem({
        'tomatoes': hyst_tomatoes,
        'beans': hyst_beans,
    })

    irrigator_system.check()
    assert switch_tomatoes.get_state() == True
    assert switch_beans.get_state() == False

    sensor_beans.set_value(5)
    irrigator_system.check()
    assert switch_tomatoes.get_state() == True
    assert switch_beans.get_state() == True

    sensor_tomatoes.set_value(45)
    sensor_beans.set_value(25)
    irrigator_system.check()
    assert switch_tomatoes.get_state() == False
    assert switch_beans.get_state() == False

def test_need_water_callback():
    sensor_tomatoes = MockMoistureSensor(value=10)
    switch_tomatoes = MockSwitch(state=False)
    hyst_tomatoes = Hysteresis(low=30, high=40, sensor=sensor_tomatoes, switch=switch_tomatoes)

    sensor_beans = MockMoistureSensor(value=20)
    switch_beans = MockSwitch(state=False)
    hyst_beans = Hysteresis(low=10, high=20, sensor=sensor_beans, switch=switch_beans)

    irrigator_system = IrrigatorSystem({
        'tomatoes': hyst_tomatoes,
        'beans': hyst_beans,
    })

    irrigator_system.check()
    assert irrigator_system.needs_water == True

    irrigator_system.check()
    assert irrigator_system.needs_water == True
    
    sensor_tomatoes.set_value(35)

    irrigator_system.check()
    assert irrigator_system.needs_water == True

