from .sensor_file import FileSensor
from .switch_file import FileSwitch
from .irrigator import Irrigator
from .irrigation_system import IrrigationSystem


class _FileSensor_Params:
    def __init__(self, filename):
        self.filename = filename
    def instantiate(self):
        return FileSensor(self.filename)

class _FileSwitch_Params:
    def __init__(self, filename):
        self.filename = filename
    def instantiate(self):
        return FileSwitch(self.filename)

class _Irrigator_Params:
    def __init__(self, name, low, high, sensor, switch):
        self.name = name
        self.low = low
        self.high = high
        self.sensor = sensor
        self.switch = switch
    def instantiate(self):
        return Irrigator(name = self.name,
                         low = self.low, 
                         high = self.high,
                         sensor = self.sensor.instantiate(),
                         switch = self.switch.instantiate())

class _IrrigationSystem_Params:
    def __init__(self, irrigators):
        self.irrigators = irrigators
    def instantiate(self):
        return IrrigationSystem([irrigator.instantiate() for irrigator in self.irrigators])

class Config:
    def __init__(self, filename):
        with open(filename) as f:
            content = f.read()

        code = compile(content, filename = filename, mode = 'exec')

        context = {
            'FileSensor': _FileSensor_Params,
            'FileSwitch': _FileSwitch_Params,
            'Irrigator': _Irrigator_Params,
            'IrrigationSystem': _IrrigationSystem_Params,
        }
        exec(code, context)

        self.irrigation_system = context['IRRIGATION_SYSTEM']

    def instantiate(self):
        return self.irrigation_system.instantiate()
