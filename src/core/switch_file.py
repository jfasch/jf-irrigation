class FileSwitch:
    def __init__(self, filename):
        self.filename = filename

    def set_state(self, state):
        with open(self.filename, 'w') as f:
            f.write(state and '1\n' or '0\n')

    def get_state(self):
        with open(self.filename) as f:
            return bool(int(f.read()))
