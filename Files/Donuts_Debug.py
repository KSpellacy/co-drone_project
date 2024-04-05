from codrone_edu.drone import *
import Color_Main

drone = Drone()


def MaxPointRun():
    ready()
    doColorStuff()
    do_movy_stuff()
    doLandingStuff()
    time.sleep(5)
    drone.disconnect()


def testAlt():
    drone.takeoff()
    drone.hover(2)
    time.sleep(1)
    drone.send_absolute_position(0, 0, 2, 1, 1, 1)
    time.sleep(4)
    drone.land()


def doLandingStuff():
    print("Im doing landing stuff!")
    Color_Main.playLandingStuff(drone)


class clr:
    def red(self: Drone):
        print("Turning Red")
        self.set_drone_LED(255, 0, 0, 100)

    def grn(self: Drone):
        print("Turning Green")
        self.set_drone_LED(0, 255, 0, 100)

    def blu(self: Drone):
        print("Turning Blue")
        self.set_drone_LED(0, 0, 255, 100)

    def wht(self: Drone):
        print("Turning White")
        self.set_drone_LED(250, 250, 250, 100)

    def blck(self: Drone):
        print("Turning Black")
        self.set_drone_LED(0, 0, 0, 100)


def doColorStuff():
    Color_Main.init_color(drone)
    time.sleep(1)
    rainbow()
    time.sleep(1)
    Color_Main.get_color(drone)
    time.sleep(3)
    clr.wht(drone)


def rainbow():
    print("Start Rainbow!")
    drone.set_drone_LED(0, 0, 0, 150)
    time.sleep(0.3)
    drone.set_drone_LED(250, 0, 0, 150)
    time.sleep(0.3)
    drone.set_drone_LED(0, 250, 0, 150)
    time.sleep(0.3)
    drone.set_drone_LED(0, 0, 250, 150)
    time.sleep(0.3)
    drone.set_drone_LED(250, 250, 250, 150)
    time.sleep(0.3)
    print("End Rainbow!")


print("Hello Drone!")


def ready():
    drone.pair()
    drone.reset_trim()
    drone.reset_sensor()
    drone.reset_move()
    return drone


def do_movy_stuff():
    drone.takeoff()
    time.sleep(2)
    drone.send_absolute_position(2.3, 0, 1.5, 0.5, 0, 0)
    time.sleep(10)
    drone.send_absolute_position(2.3, 1.8, 1.5, 0.5, 0, 0)
    time.sleep(3)
    drone.land()
    time.sleep(3)


MaxPointRun()
