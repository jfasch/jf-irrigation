from core.switch_mock import MockSwitch


def test_mock_switch():
    switch = MockSwitch(state=False)
    assert switch.get_state() == False

    switch.set_state(True)
    assert switch.get_state() == True

    switch.set_state(False)
    assert switch.get_state() == False
