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
Color_Main.play(drone)
drone.reset_move()
time.sleep(2)
drone.takeoff()
time.sleep(2)

drone.send_absolute_position(2.5, 0, 1.5, 1, 0, 0)
time.sleep(4)
drone.send_absolute_position(2.5, 1.6, 1.4, 1, 0, 0)
time.sleep(4)
drone.send_absolute_position(2.5, 1.6, 0.2, .5, 0, 0)
time.sleep(4)

drone.stop_motors()

Color_Main.play2(drone)
drone.disconnect()

#SPELLACY HELP US - colours
# if Spellacy helps us with colours:
#     drone.takeoff()
#     drone.send_absolute_position(0,0.5,0.5,1set_drone_LED(0, 128, 0, 150)  # green,0,0)
#     drone.land()
# else :
#     drone.takeoff()
#     drone.send_absolute_position(0,-0.5,0.5,1,0,0)
#     drone.land()

