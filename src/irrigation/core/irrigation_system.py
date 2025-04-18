class IrrigationSystem:
    def __init__(self, irrigators):
        self.irrigators = { ir.name: ir for ir in irrigators }
        self.needs_water = False

    def get_irrigator_names(self):
        return list(self.irrigators.keys())

    def get_irrigator(self, name):
        return self.irrigators[name]

    def check(self):
        self.needs_water = False
        for irrigator in self.irrigators.values():
            irrigator.check()
            if irrigator.switch.get_state() == True:
                self.needs_water = True

    
