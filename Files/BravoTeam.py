from codrone_edu.drone import *

drone = Drone()
drone.load_classifier(dataset="color_data")
drone.set_drone_LED(255, 255, 255, 255)
time.sleep(1)
drone.pair()


def set_color():
    color_data = drone.get_color_data()

    color = drone.predict_colors(color_data)
    if color[0] == "red":
        drone.set_drone_LED(255, 0, 0, 150)  # red

    elif color[0] == "lightblue":
        drone.set_drone_LED(0, 0, 255, 150)  # blue

    elif color[0] == "green":
        drone.set_drone_LED(0, 128, 0, 150)  # green
    elif color[0] == "purple":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    elif color[0] == "blue":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    elif color[0] == "yellow":
        drone.set_drone_LED(0, 255, 0, 150)  # green
    elif color[0] == "black":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    elif color[0] == "white":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    else:
        drone.set_drone_LED(0, 0, 0, 0)  # black
    return color[0]


set_color()
drone.takeoff()
time.sleep(2)
drone.send_absolute_position(2.3, 0, 1.5, 0.5, 0, 0)
time.sleep(10)
drone.send_absolute_position(2.3, 1.7, 1.5, 0.5, 0, 0)
time.sleep(10)

drone.land()
color = set_color()
time.sleep(2)
drone.takeoff()
time.sleep(2)
print("Color = " + color)
if color == "blue" or color == "lightblue":
    drone.set_pitch(20)
    drone.move(.1)
elif color == "red":
    drone.set_pitch(-20)
    drone.move(.1)
else:
    drone.set_roll(20)
    drone.move(.1)
time.sleep(2)
drone.land()
drone.disconnect()