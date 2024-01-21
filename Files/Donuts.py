from codrone_edu.drone import *
import Color_Main


def pair():
    drone = Drone()
    drone.pair()
    drone.reset_trim()
    drone.reset_sensor()
    drone.reset_move()
    return drone


def to_second_arch(drone):
    drone.send_absolute_position(2.5, 0, 1.6, 1, 0, 0)


drone = pair()


def hover(drone):
    drone.hover(5)


# Color_Main.play()

# takeoff
drone.takeoff()
time.sleep(2)
# through first keyhole

drone.send_absolutce_position(1.5, 0, 1.6, 1, 0, 0)
time.sleep(2)
drone.get_position_data()
hover(drone)

drone.circle()
drone.send_absolute_position(1.5, 0, 2.1, 1, 0, 0)
hover(drone)


drone.land()
drone.disconnect()


# drone.send_absolute_position(3.04, 1.8, 1, 1, 0, 0)

