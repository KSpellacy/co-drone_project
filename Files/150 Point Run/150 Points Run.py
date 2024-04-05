from codrone_edu.drone import *
import Color_Main

color_data = None
drone = Drone()
drone.pair()


class color:

    def red(self: Drone):
        self.set_drone_LED(255, 0, 0, 100)
        print("Turning Red")

    def grn(self: Drone):
        self.set_drone_LED(0, 255, 0, 100)
        print("Turning Green")

    def blu(self: Drone):
        self.set_drone_LED(0, 0, 255, 100)
        print("Turning Blue")

    def wht(self: Drone):
        self.set_drone_LED(250, 250, 250, 100)
        print("Turning White")

    def blck(self: Drone):
        self.set_drone_LED(0, 0, 0, 100)
        print("Turning Black")

    def ylw(self: Drone):
        self.set_drone_LED(255,255,0,100)
        print("Turning Yellow")


def rainbow():
    print("Start Rainbow!")
    color.blck(drone)
    time.sleep(0.1)
    color.wht(drone)
    time.sleep(0.1)
    color.blu(drone)
    time.sleep(0.1)
    color.grn(drone)
    time.sleep(0.1)
    color.red(drone)
    time.sleep(0.1)
    print("End Rainbow!")


def moreColorCrap():
    Color_Main.init_color(drone)
    Color_Main.get_color(drone)


def takeOffCode():
    rainbow()
    moreColorCrap()
    drone.takeoff()
    print(drone.get_position_data())
    drone.send_absolute_position(0, 0, 1.5, 1, 0, 0)


def thr_Loop():
    color.grn(drone)
    drone.send_absolute_position(0, 0, 1.5, 1, 0, 0)
    color.blu(drone)
    drone.set_pitch(85)
    drone.move(2)


def mvThoughKeyHoley(apricot: Drone):
    color.grn(apricot)
    apricot.send_absolute_position(2.8, 0, 1.5, 1, 0, 0)
    color.ylw(apricot)
    time.sleep(2)
    color.red(apricot)


def loopingCrap():
    while True:
        mvThoughKeyHoley(drone)
        for i in range(1, 4):
            print("run ", str(i + 1))
            thr_Loop()


def play():
    takeOffCode()
    color.blu(drone)
    print("Drone Moving Up")
    time.sleep(2)
    loopingCrap()
    color.grn(drone)
    drone.land()


def main():
    x = drone.get_battery()
    print("The battery is at ", x, "%")
    if x >= 80:
        play()

    elif x < 80:
        drone.disconnect()
        print("Please get new battery. The battery is below 80%")


main()

print("Potato: Aiden Minick")
