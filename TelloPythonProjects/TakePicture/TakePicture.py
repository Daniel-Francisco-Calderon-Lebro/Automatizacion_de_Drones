import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()
tello.streamon()

frame_read = tello.get_frame_read()

tello.takeoff()
tello.move_up(30)

# cv2.imwrite("picture.jpeg", frame_read.frame)
cv2.imwrite("picture.jpeg", cv2.cvtColor(frame_read.frame, cv2.COLOR_RGB2BGR))

tello.land()