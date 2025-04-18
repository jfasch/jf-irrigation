class StdOutSwitch:
    def __init__(self, prefix):
        self.prefix = prefix
        self.state = False
    def get_state(self):
        return self.state
    def set_state(self, state):
        if self.state == state:
            print(self.prefix, '(noop)')
        else:
            self.state = state
            print(self.prefix, '->', state)
