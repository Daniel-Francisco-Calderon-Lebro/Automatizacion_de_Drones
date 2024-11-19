from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()
img = me.get_frame_read().frame
me.takeoff()
while True:
    
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    
    
    if cv2.waitKey(1) == ord('q'):
        me.streamoff()
        me.land()
        break

