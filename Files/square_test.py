import time

from codrone_edu.drone import *
from loopdedoop import *

"""
Test for loopdedoop; supposed to takeoff, fly forward, do a square to the right, then go
backwards and land. It keeps the absolute position decently.
"""


drone = Drone()
drone.pair()

drone.takeoff()
time.sleep(1)

drone.send_absolute_position(0.5, 0, 1, 1, 0, 0)
time.sleep(2)
drone.reset_move()
time.sleep(1)

loop_to_right(drone)

drone.send_absolute_position(-1, 0, 1, 1, 0, 0)
time.sleep(2)

drone.land()