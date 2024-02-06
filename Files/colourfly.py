from codrone_edu.drone import *
from Color_Main import *


def pair():
    drone = Drone()
    drone.pair()
    drone.reset_trim()
    drone.reset_sensor()
    drone.reset_move()
    return drone


drone = pair()

drone.takeoff()
drone.send_absolute_position(2, 0, 1, 1, 0, 0)
drone.send_absolute_position(2, 2, 1, 1, 0, 0)
drone.land()

# get_color(drone)

# if color[0] == "red":
#     drone.send_absolute_position(0,0.5,1,1,0,0)
#     drone.land()
#
# if color[0] == "green":
#     drone.send_absolute_position(1,0,0.5,1,0,0)
#     drone.land()
#
# if color[0] == "blue":
#     drone.send_absolute_position(0,-0.5,1,1,0,0)
#     drone.land()
