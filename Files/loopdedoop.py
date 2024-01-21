from codrone_edu.drone import *

"""
Supposed to loop a keyhole with drone directly in front of hole. Works fine. Changing speed
and seconds will affect where you end up.
"""

default_speed = 85
default_seconds = 1
#adj for different radi

def _loop(drone: Drone, direction: int = 1):
    drone.square(default_speed, default_seconds, direction)
    print('after square:', drone.get_position_data())
    drone.hover(2)
    drone.reset_move()
    time.sleep(1)
    print('after sleep:', drone.get_position_data())


def loop_to_right(drone: Drone):
    _loop(drone, 1)


def loop_to_left(drone: Drone):
    _loop(drone, -1)
