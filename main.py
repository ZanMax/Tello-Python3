from time import sleep

import cv2
from djitellopy import tello

from controller import move

drone_speed = 60
critical_temperature = 85
takeoff_status = False

drone = tello.Tello()
drone.connect()

battery = drone.get_battery()
print("Battery level:", battery, "%")

if int(battery) < 25:
    print("--> Low battery level")
    exit()

temperature_low = drone.get_lowest_temperature()
temperature_max = drone.get_highest_temperature()
print("Temperature: {} - {} °C".format(temperature_low, temperature_max))

if temperature_max >= critical_temperature:
    print("--> Critical temperature")
    exit()

drone.streamon()

while True:

    image = drone.get_frame_read().frame
    cv2.imshow('Image', image)
    # key = cv2.waitKey(1) & 0xFF

    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(image, str(battery), (100, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

    key = cv2.waitKeyEx(1)

    if takeoff_status:
        mv = move(key, drone_speed)
        drone.send_rc_control(mv[0], mv[1], mv[2], mv[3])
        sleep(0.08)

    if key == ord('0'):
        drone.land()
        takeoff_status = False

    if key == ord('1'):
        if not takeoff_status:
            drone.takeoff()
            sleep(1)
            takeoff_status = True

    if key == ord('q'):
        drone.streamoff()
        break
    if key == 27:
        drone.emergency()

    if key == 61:
        if drone_speed < 100:
            drone_speed += 10
    if key == 45:
        if drone_speed > 10:
            drone_speed -= 10

    if key == ord('i'):
        battery = drone.get_battery()
        height = drone.get_height()
        distance = drone.get_distance_tof()
        title = 'Battery: {} | Speed: {} | Height: {} | Distance: {}'.format(battery, drone_speed, height, distance)
        cv2.setWindowTitle('Image', title)

cv2.destroyAllWindows()
