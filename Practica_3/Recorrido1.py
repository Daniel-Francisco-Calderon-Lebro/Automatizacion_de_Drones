from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
import time
if __name__ == '__main__':

    # sim_key = '6275c978-ccea-41a1-b88a-4e258985d273'
    sim_key = None
    
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff() #despega a 78cms real 58 simulado
        #Rojo inicia 78cm
        drone.fly_up(114, 'cm')
        drone.fly_forward(150, 'cm')
        # drone.fly_forward(75, 'cm')
        #Blanco
        drone.yaw_left(90)
        drone.fly_forward(90, 'cm')
        drone.yaw_right(90)

        drone.fly_down(38, 'cm' )
        drone.fly_forward(150, 'cm' )
        # drone.fly_forward(75, 'cm')

        drone.yaw_right(90)
        drone.fly_forward(90, 'cm' )
        drone.yaw_left(90)

        drone.fly_down(35, 'cm' )
        drone.fly_forward(150, 'cm')
        # drone.fly_forward(75, 'cm')


        #Verde
        drone.yaw_left(90)
        drone.fly_forward(90, 'cm')
        drone.yaw_right(90)

        drone.fly_up(42, 'cm')
        drone.fly_forward(150, 'cm')
        # drone.fly_forward(75, 'cm')
        drone.yaw_right(90)
        drone.fly_forward(90, 'cm')
        drone.yaw_right(90)
        drone.fly_up(20, 'cm')
        drone.fly_forward(600, 'cm')
        

        #aro1 107 centimetros de base y diametro interior 32cm amarillo  107+16=123
        #aro2 137 centimetros de base y diametro interior 32cm blanco    137+16=153
        #aro3 155 centimetros de base y diametro interior 40cm verde     155+20=175
        #aro4 176 centimetros de base y diametro interior 27cm rojo      176+13=189
        # time.sleep(5)
        # secuencia de recorrido son 8 segmentos hay aros en 1, 
        drone.land()

        