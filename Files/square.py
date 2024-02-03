from codrone_edu.drone import *
import loopdedoop
import Color_Main
import time
import Rick_Roll

"""
Test for loopdedoop; supposed to takeoff, fly forward, do a square to the right, then go
backwards and land. It keeps the absolute position decently.
"""

class colors:
    def red(drone: Drone):
        drone.set_drone_LED(150, 0, 0, 150)
    def blue(drone: Drone):
        drone.set_drone_LED(0, 0, 150, 150)

    def black(drone: Drone):
        drone.set_drone_LED(0, 0, 0, 150)

    def green(drone: Drone):
        drone.set_drone_LED(0, 150, 0, 150)


drone = Drone()
drone.pair()

Color_Main.init_color(drone)

Color_Main.get_color(drone)
time.sleep(2)

drone.takeoff()
time.sleep(1)
colors.red(drone)

drone.send_absolute_position(1.50, 0, 1.26, 1, 0, 0)
time.sleep(2)
# drone.send_absolute_position(4,0,0,0,0,0)
colors.blue(drone)
time.sleep(4)
colors.green(drone)

loopdedoop.loop_to_right(drone)

#drone.send_absolute_position(1.25, 0, 0, 1, 0, 0)
# drone.move_forward(75, "cm", 0.50)
drone.send_absolute_position(1.9,0,1,1,0,0)
time.sleep(3)
drone.send_absolute_position(0,0,1.5,1,0,0)
time.sleep(5)
colors.black(drone)
drone.land()
Rick_Roll.play(drone)
