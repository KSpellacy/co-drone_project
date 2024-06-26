from codrone_edu.drone import *

color_data = None
drone = Drone()


def init_color(a_drone: Drone):
    print("Init")
    a_drone.load_classifier(dataset="color_data")
    global color_data


def get_color(drone):
    print("get_color")
    time.sleep(0.5)
    global color_data
    color_data = drone.get_color_data()
    da_color = drone.predict_colors(color_data)
    print(da_color)

    if da_color[0] == "red":
        drone.set_drone_LED(255, 0, 0, 150)  # red

    elif da_color[0] == "lightblue":
        drone.set_drone_LED(0, 0, 255, 150)  # blue

    elif da_color[0] == "green":
        drone.set_drone_LED(0, 128, 0, 150)  # green
    elif da_color[0] == "purple":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    elif da_color[0] == "blue":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    elif da_color[0] == "yellow":
        drone.set_drone_LED(0, 255, 0, 150)  # green
    elif da_color[0] == "black":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    elif da_color[0] == "white":
        drone.set_drone_LED(0, 0, 255, 150)  # blue
    else:
        drone.set_drone_LED(0, 0, 0, 0)  # black


def set_color():
    color_data = drone.get_color_data()


color = set_color()


def playLandingStuff(drone):
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


"""global color_data
    color_data = drone.get_color_data()
    color = drone.predict_colors(color_data)
"""
