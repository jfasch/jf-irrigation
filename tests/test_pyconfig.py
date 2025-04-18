from core.config import PyConfig

import pytest

@pytest.fixture
def _configfile_standard(tmpdir):
    with open(tmpdir / 'tomatoes-moisture', 'w') as f: f.write('40\n')
    with open(tmpdir / 'beans-moisture', 'w') as f: f.write('20\n')
    with open(tmpdir / 'tomatoes-switch', 'w') as f: f.write('0\n')
    with open(tmpdir / 'beans-switch', 'w') as f: f.write('0\n')

    dname = str(tmpdir)

    content = [
        f"sensor_tomatoes = FileSensor('{dname}/tomatoes-moisture')",
        f"sensor_beans = FileSensor('{dname}/beans-moisture')",
        f"switch_tomatoes = FileSwitch('{dname}/tomatoes-switch')",
        f"switch_beans = FileSwitch('{dname}/beans-switch')",

        "irrigator_tomatoes = Irrigator(name='tomatoes', low=50, high=60, sensor=sensor_tomatoes, switch=switch_tomatoes)",
        "irrigator_beans = Irrigator(name='beans', low=30, high=40, sensor=sensor_beans, switch=switch_beans)",

        "IRRIGATION_SYSTEM = IrrigationSystem((irrigator_tomatoes, irrigator_beans))",
    ]
    with open(tmpdir / 'config.conf', 'w') as f:
        f.write('\n'.join(content))

    return tmpdir / 'config.conf'

def test_full_system(_configfile_standard):
    config = PyConfig(_configfile_standard)

    irrigation_system = config.instantiate()

    irrigator_tomatoes = irrigation_system.get_irrigator('tomatoes')
    assert irrigator_tomatoes.name == 'tomatoes'
    assert irrigator_tomatoes.low == pytest.approx(50)
    assert irrigator_tomatoes.high == pytest.approx(60)
    assert irrigator_tomatoes.sensor.get_value() == pytest.approx(40)
    assert irrigator_tomatoes.switch.get_state() == False

    irrigator_beans = irrigation_system.get_irrigator('beans')
    assert irrigator_beans.name == 'beans'
    assert irrigator_beans.low == pytest.approx(30)
    assert irrigator_beans.high == pytest.approx(40)
    assert irrigator_beans.sensor.get_value() == pytest.approx(20)
    assert irrigator_beans.switch.get_state() == False
