def move(key, speed):
    lr, fb, ud, yv = 0, 0, 0, 0

    if 10 < speed > 100:
        print("Speed must be between 10 and 100")
        speed = 20

    if key == ord('w'):
        ud = speed
    if key == ord('s'):
        ud = -speed
    if key == ord('a'):
        yv = -speed
    if key == ord('d'):
        yv = speed

    if key == 63232:
        fb = speed
    if key == 63233:
        fb = -speed
    if key == 63234:
        lr = -speed
    if key == 63235:
        lr = speed

    return [lr, fb, ud, yv]
