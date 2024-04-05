from codrone_edu.drone import *


def pair():
    drone = Drone()
    drone.pair()
    drone.reset_trim()
    drone.reset_sensor()
    drone.reset_move()
    return drone


drone = pair()

drone.takeoff()


def flythroughredarch(drone: Drone):
    drone.send_absolute_position(2.5, 0, 1.4, 1, 0, 0)


def flythroughyellowhoop(drone: Drone):


def flythroughgreenhoop(drone: Drone):


def flythroughbluearch(drone: Drone):



flythroughredarch(