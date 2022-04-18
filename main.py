from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()

battery = drone.get_battery()
bar = drone.get_barometer()
print(battery)
print(bar)

drone.streamon()
while True:
    image = drone.get_frame_read().frame
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        drone.streamoff()
        break
    if key == ord('b'):
        battery = drone.get_battery()
        print(battery)
        cv2.setWindowTitle('Image', 'Battery: {}'.format(battery))
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(image, str(battery), (100, 50), font, 1, (0, 255, 0), 1, cv2.LINE_AA)

cv2.destroyAllWindows()
