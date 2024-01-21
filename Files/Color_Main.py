from codrone_edu.drone import *

color_data = None


def init_color(drone: Drone):
    print("Init")
    drone.load_classifier(dataset="color_data")
    global color_data


def get_color(drone):
    print("get_color")
    time.sleep(0.5)
    global color_data
    color_data = drone.get_color_data()
    color = drone.predict_colors(color_data)
    print(color)

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
