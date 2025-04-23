class IrrigationSystem:
    def __init__(self, irrigators):
        self.irrigators = { ir.name: ir for ir in irrigators }

    def get_irrigator_names(self):
        return list(self.irrigators.keys())

    def get_irrigator(self, name):
        return self.irrigators[name]

    def check(self):
        new_switch_states = {}
        for irrigator in self.irrigators.values():
            new_switch_state = irrigator.check()
            if new_switch_state is not None:
                new_switch_states[irrigator.name] = new_switch_state
        return new_switch_states
