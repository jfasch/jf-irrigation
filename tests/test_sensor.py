from core.sensor_mock import MockSensor
from core.sensor_random import RandomSensor
from core.sensor_file import FileSensor

import pytest


def test_mock():
    sensor = MockSensor(value=30)
    assert pytest.approx(sensor.get_value()) == 30.0

    sensor.set_value(42.7)
    assert pytest.approx(sensor.get_value()) == 42.7

def test_random():
    sensor = RandomSensor(low=0.0, high=100.0)
    assert 0.0 <= sensor.get_value() <= 100.0

def test_file(tmpdir):
    with open(tmpdir / 'moisture', 'w') as moifile:
        moifile.write('42.666')
    sensor = FileSensor(tmpdir / 'moisture')
    assert pytest.approx(sensor.get_value()) == 42.666
    
