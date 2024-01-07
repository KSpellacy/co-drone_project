from codrone_edu.drone import *
import Color_Main


def pair():
    drone = Drone()
    drone.pair()
    drone.reset_trim()
    drone.reset_sensor()
    drone.reset_move()
    return drone


drone = pair()

Color_Main.play()
drone.takeoff()
time.sleep(5)

drone.send_absolute_position(3.04, 0, 1.6, 1, 0, 0)
time.sleep(5)
drone.send_absolute_position(3.04, 1.8, 1, 1, 0, 0)
time.sleep(5)

drone.land()
drone.disconnect()
