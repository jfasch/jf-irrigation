from irrigation.core.sensor_mock import MockSensor
from irrigation.core.switch_mock import MockSwitch
from irrigation.core.irrigator import Irrigator

import pytest


def test_basic():
    sensor = MockSensor(value=42)
    switch = MockSwitch(state=False)

    irrigator = Irrigator(
        name = 'tomatoes',
        low = 20,
        high = 40,
        sensor = sensor,
        switch = switch,
    )

    irrigator.check()
    
    assert irrigator.switch.get_state() == False

def test_switch_changed_info():
    sensor = MockSensor(value=42)
    switch = MockSwitch(state=False)

    irrigator = Irrigator(
        name = 'tomatoes',
        low = 20,
        high = 40,
        sensor = sensor,
        switch = switch,
    )

    new_switch_state = irrigator.check()    # nothing to do
    assert new_switch_state is None

    sensor.set_value(10)      # below low -> need water
    new_switch_state = irrigator.check()
    assert new_switch_state == True
    
    sensor.set_value(30)      # right in the middle
    new_switch_state = irrigator.check()
    assert new_switch_state is None

    sensor.set_value(50)      # saturated
    new_switch_state = irrigator.check()
    assert new_switch_state == False

def test_public_iface_for_dbus():
    sensor = MockSensor(value=42)
    switch = MockSwitch(state=False)

    irrigator = Irrigator(
        name = 'tomatoes',
        low = 20,
        high = 40,
        sensor = sensor,
        switch = switch,
    )

    # publicly exposed
    irrigator.check()
    assert irrigator.sensor is sensor
    assert irrigator.switch is switch
    assert pytest.approx(irrigator.low) == 20
    assert pytest.approx(irrigator.high) == 40
