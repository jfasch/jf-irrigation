from core.moisture_mock import MockMoistureSensor
from core.switch_mock import MockSwitch
from core.irrigator import Irrigator

import pytest


def test_basic():
    sensor = MockMoistureSensor(value=42)
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

def test_public_iface_for_dbus():
    sensor = MockMoistureSensor(value=42)
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
