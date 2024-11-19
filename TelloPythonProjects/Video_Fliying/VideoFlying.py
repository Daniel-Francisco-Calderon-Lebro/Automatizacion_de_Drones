from djitellopy import Tello
import cv2
import time
from threading import Thread
speed = 25

tello = Tello()
tello.connect()
print(tello.get_battery())
tello.streamon()
frame_read = tello.get_frame_read()

def main():
    while True:
        tello.takeoff()
        if not tello.is_flying:
            tello.takeoff()
        up_flag = True
        t1 = time.time()
        while True:
            if time.time() - t1 > 3:
                t1 = time.time()
                if up_flag:
                    up_flag = False
                    tello.send_rc_control(0, 0, speed, 0)
                else:
                    up_flag = True
                    tello.send_rc_control(0, 0, -speed, 0)




def grabar():  
    while True:
        tello_video_image = cv2.cvtColor(frame_read.frame, cv2.COLOR_RGB2BGR)
        if tello_video_image is not None:
            cv2.imshow("TelloVideo", tello_video_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    tello.land()
    tello.streamoff()
    cv2.destroyAllWindows()
    
    flight_grabar_thread.join()
    # flight_pattern_thread.join()

# flight_pattern_thread = Thread(target=flight_pattern, daemon=True)
# flight_pattern_thread.start()
flight_grabar_thread = Thread(target=grabar, daemon=True)
flight_grabar_thread.start()

if __name__ == "__main__":
    main()