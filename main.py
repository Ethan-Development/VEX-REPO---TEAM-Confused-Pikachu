###
# TEAM SURPRISED PIKACHU - MAIN RUNCODE
# WRITTEN BY ETHAN YIP, AARON D'SOUZA
# DOCUMENTATION BY ETHAN YIP
# 4/5/2025 - 5/XX/2025
###

import time
import random
import sys
import math

sys.path.append('../')
from motors.camera import camera
from motors.motorA import A
from motors.motorB import B
from motors.motorC import C
from motors.motorD import D

from control.control import automv
from control.control import manmv

from vex import *

if __name__ == "__main__":
    brain=Brain()
    brain.screen.print("Hello V5")
    
    camera(0, 0, True)

