from codrone_edu.drone import *
import Color_Main


def rainbow(a_drone: Drone):
    a_drone.set_drone_LED(0, 0, 0, 150)
    time.sleep(0.3)
    a_drone.set_drone_LED(250, 0, 0, 150)
    time.sleep(0.3)
    a_drone.set_drone_LED(0, 250, 0, 150)
    time.sleep(0.3)
    a_drone.set_drone_LED(0, 0, 250, 150)
    time.sleep(0.3)
    a_drone.set_drone_LED(250, 250, 250, 150)
    time.sleep(0.3)


print("Hello World!")


def ready():
    a_drone = Drone()
    a_drone.pair()
    rainbow(a_drone)
    Color_Main.init_color(a_drone)
    a_drone.reset_trim()
    a_drone.reset_sensor()
    a_drone.reset_move()
    return a_drone


drone = ready()

"""
drone.set_drone_LED(0,0,0,150)
time.sleep(1)
Color_Main.get_color(drone)
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

drone.land()

drone.send_absolute_position(2.5, 0, 1.5, 1, 0, 0)
time.sleep(4)
drone.send_absolute_position(2.5, 1.6, 1.4, 1, 0, 0)
time.sleep(4)
drone.send_absolute_position(2.5, 1.6, 0.2, .5, 0, 0)
drone.stop_motors()

"""

#  Color_Main.play_Willis_Pain(drone)
drone.disconnect()
