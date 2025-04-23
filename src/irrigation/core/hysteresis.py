class Hysteresis:
    def __init__(self, low, high, sensor, switch):
        self.low = low
        self.high = high
        self.sensor = sensor
        self.switch = switch

    def check(self):
        value = self.sensor.get_value()
        old_state = self.switch.get_state()

        if value < self.low:
            new_state = True
        elif value > self.high:
            new_state = False
        else:
            new_state = old_state

        if new_state != old_state:
            self.switch.set_state(new_state)
            return new_state
        else:
            return None
