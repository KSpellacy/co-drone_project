from codrone_edu.drone import *
from Files import Color_Main

drone = Drone()
drone.pair()

while True:
    Color_Main.play(drone)
