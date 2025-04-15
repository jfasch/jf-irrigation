import pytest

from core.moisture_mock import MockMoistureSensor
from core.moisture_random import RandomMoistureSensor


def test_mock_moisture_sensor():
    sensor = MockMoistureSensor(value=30)
    assert pytest.approx(sensor.get_value()) == 30.0

    sensor.set_value(42.7)
    assert pytest.approx(sensor.get_value()) == 42.7

def test_random_moisture_sensor():
    sensor = RandomMoistureSensor(low=0.0, high=100.0)
    assert 0.0 <= sensor.get_value() <= 100.0
