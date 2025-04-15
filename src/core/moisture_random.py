import random


class RandomMoistureSensor:
    def __init__(self, low, high):
        self.low = low
        self.high = high
    def get_value(self):
        return random.uniform(self.low, self.high)
