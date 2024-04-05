from codrone_edu.drone import *
import Color_Main
color_data = None
drone = Drone()


def thr_Loop():
    drone.send_absolute_position(2.2, 0, 1.5, 0.3, 0, 0)
    time.sleep(5)
    drone.send_absolute_position(0, 0, 1.5, 0.3, 0, 0)
    time.sleep(5)


def colorCrap():
    Color_Main.init_color(drone)
    Color_Main.get_color(drone)


def loopingCrap():
    for i in range(4):
        thr_Loop()


def main():
    colorCrap()
    drone.takeoff()
    loopingCrap()
    drone.land()


main()

