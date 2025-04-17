class IrrigatorSystem:
    def __init__(self, irrigators):
        self.irrigators = irrigators
        self.needs_water = False

    def check(self):
        self.needs_water = False
        for irrigator in self.irrigators:
            irrigator.check()
            if irrigator.switch.get_state() == True:
                self.needs_water = True

    
