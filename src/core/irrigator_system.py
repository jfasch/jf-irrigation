class IrrigatorSystem:
    def __init__(self, irrigators):
        self.irrigators = irrigators
        self.needs_water = False

    def check(self):
        self.needs_water = False
        for hysteresis in self.irrigators.values():
            hysteresis.check()
            if hysteresis.switch.get_state() == True:
                self.needs_water = True

    
