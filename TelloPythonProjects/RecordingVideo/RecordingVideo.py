import time
import cv2
from threading import Thread
from djitellopy import Tello

# Conectar el dron
tello = Tello()
tello.connect()

# Activar el stream de video
tello.streamon()
frame_read = tello.get_frame_read()

# Variable de control para grabar
keepRecording = True

def videoRecorder():
    # Esperar hasta que el primer frame esté disponible
    while frame_read.frame is None:
        time.sleep(0.1)
    
    # Crear el objeto VideoWriter para grabar el video
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))
    
    while keepRecording:
        # Verificar que el frame no sea None antes de escribirlo
        if frame_read.frame is not None:
            video.write(frame_read.frame)
        else:
            print("Frame no disponible.")
        time.sleep(1 / 10)

    # Liberar el objeto VideoWriter
    video.release()
    print("Grabación finalizada y archivo de video liberado.")

# Crear y ejecutar el hilo para la grabación de video
recorder = Thread(target=videoRecorder, daemon=True)
recorder.start()

# Ejecución de comandos de vuelo
tello.takeoff()
tello.rotate_counter_clockwise(360)
tello.land()

# Detener la grabación
keepRecording = False
recorder.join()

# Detener el stream de video y liberar recursos
tello.streamoff()
print("Streaming detenido.")
