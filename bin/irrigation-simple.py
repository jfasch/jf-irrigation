#!/usr/bin/env python3

from core.moisture_file import FileMoistureSensor
from core.switch_stdout import StdOutSwitch
from core.irrigation_system import IrrigationSystem
from core.irrigator import Irrigator

import time
import argparse


parser = argparse.ArgumentParser(description='Irrigation system.')
parser.add_argument('--pyconfigfile')
args = parser.parse_args()

conf = PyConfig(args.pyconfigfile)

sensors = make_sensors(conf)
switches = make_switches(conf)
irrigators = make_irrigators(conf, sensors=sensors, switches=switches)

irrigation = IrrigationSystem(irrigators)

while True:
    time.sleep(1)
    irrigation.check()
