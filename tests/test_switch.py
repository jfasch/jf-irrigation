from core.switch_mock import MockSwitch
from core.switch_file import FileSwitch


def test_mock_switch():
    switch = MockSwitch(state=False)
    assert switch.get_state() == False

    switch.set_state(True)
    assert switch.get_state() == True

    switch.set_state(False)
    assert switch.get_state() == False

def test_file_switch(tmpdir):
    with open(tmpdir / 'switch', 'w') as f:
        f.write('0\n')

    switch = FileSwitch(tmpdir / 'switch')
    assert switch.get_state() == False

    switch.set_state(True)
    with open(tmpdir / 'switch') as f:
        assert bool(int(f.read())) == True
    assert switch.get_state() == True

    switch.set_state(False)
    with open(tmpdir / 'switch') as f:
        assert bool(int(f.read())) == False
    assert switch.get_state() == False

