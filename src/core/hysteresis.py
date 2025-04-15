class Hysteresis:
    def __init__(self, low, high, sensor, switch):
        self.low = low
        self.high = high
        self.sensor = sensor
        self.switch = switch

    def check(self):
        value = self.sensor.get_value()
        if value < self.low:
            self.switch.set_state(True)
        elif value > self.high:
            self.switch.set_state(False)
        else: 
            pass
