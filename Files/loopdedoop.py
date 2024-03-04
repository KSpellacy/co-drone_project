from codrone_edu.drone import *

"""
Supposed to loop a keyhole with drone directly in front of hole. Works fine. Changing speed
and seconds will affect where you end up.
"""

default_speed = 70
default_seconds = 0.7
#adj for different radi

def _loop(drone: Drone, direction: int = 1):
    drone.square(default_speed, default_seconds, direction)


    drone.set_roll(40)
    drone.move(0.2)
    drone.set_roll(-45)
    drone.move(0.1)
    drone.reset_move()

    print('after square:', drone.get_position_data())
    print('after sleep:', drone.get_position_data())


def loop_to_right(drone: Drone):
    _loop(drone, 1)


def loop_to_left(drone: Drone):
    _loop(drone, -1)
