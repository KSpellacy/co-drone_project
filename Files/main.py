from codrone_edu.drone import *
from Files import Color_Main
import Rick_Roll

drone = Drone()
drone.pair()

# Rick_Roll.play(drone)
# #time.sleep(5)


Color_Main.init_color(drone)

while True:
    # todo Make a for loop to take an average of five runs of the colorMain so that it doesn't flicker
    Color_Main.get_color(drone)
