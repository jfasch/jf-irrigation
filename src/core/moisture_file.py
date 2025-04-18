class FileMoistureSensor:
    def __init__(self, filename):
        self.filename = filename

    def get_value(self):
        with open(self.filename) as f:
            return float(f.read())
