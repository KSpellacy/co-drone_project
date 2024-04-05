def thr_Loop():
    drone.send_absolute_position(2.2, 0, 1.3, 1, 0, 0)
    drone.hover(2)
    time.sleep(2)
    drone.send_absolute_position(0, 0, 1.3, 1, 0, 0)
    drone.hover(2)
    time.sleep(2)