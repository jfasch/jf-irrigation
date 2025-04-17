from .hysteresis import Hysteresis


class Irrigator:
    def __init__(self, name, low, high, sensor, switch):
        self.name = name
        self.hysteresis = Hysteresis(low=low, high=high, sensor=sensor, switch=switch)

    def check(self):
        self.hysteresis.check()

    @property
    def sensor(self):
        return self.hysteresis.sensor
    @property
    def switch(self):
        return self.hysteresis.switch
