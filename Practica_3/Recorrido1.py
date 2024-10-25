from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
import time
if __name__ == '__main__':
    """Secuencia de recorrido
    Secuencia de Obstaculos:
    1. Verde
    2. Rojo
    3. Blanco
    4. Amarillo
    
    Alturas:
        Obstaculo #1 155 centimetros de base y diametro interior 40cm verde     155+20=175
        Obstaculo #2 176 centimetros de base y diametro interior 27cm rojo      176+13=189
        Obstaculo #3 137 centimetros de base y diametro interior 32cm blanco    137+16=153
        Obstaculo #4 107 centimetros de base y diametro interior 32cm amarillo  107+16=123
    
    Altura de paso
         Obstaculo #1 desde el suelo = 175
         Obstaculo #2 desde el suelo = 189
         Obstaculo #3 desde el suelo = 153
         Obstaculo #4 desde el suelo = 123

    Altura de vuelo primer todos los obstaculos
        Altura inicial de despegue = 78
        Alrura de vuelo paso del obstaculo #1 = 175 - 78 = 97 con una correccion +- 3
        Alrura de vuelo paso del obstaculo #2 = 189 - 78 = 111 con una correccion +- 3
        Alrura de vuelo paso del obstaculo #3 = 153 - 78 = 75 con una correccion +- 3
        Alrura de vuelo paso del obstaculo #4 = 123 - 78 = 45 con una correccion +- 3

    Secuencia de recorrido:
        despegue de 78cm        #segmento 1 Altura real 78
        suba 97cm               #segmento 1 Altura real 175
        avance 150cm            #segmento 1 Altura real 175 
        gira 90 grados izq      #segmento 1 Altura real 175 #s1 fin
        avance 150cm            #segmento 2 Altura real 175
        gira 90 grados der      #segmento 2 Altura real 175 #s2 fin
        suba 14cm               #segmento 2 Altura real 189
        avance 150cm            #segmento 3 Altura real 189
        gira 90 grados der      #segmento 3 Altura real 189 #s3 fin
        avance 150cm            #segmento 4 Altura real 189
        gira 90 grados izq      #segmento 4 Altura real 189 #s4 fin
        baja 36cm               #segmento 4 Altura real 153
        avance 150cm            #segmento 5 Altura real 153 
        gira 90 grados izq      #segmento 5 Altura real 153 #s5 fin
        avance 150cm            #segmento 6 Altura real 153
        gira 90 grados der      #segmento 6 Altura real 153 #s6 fin
        baja 30cm               #segmento 6 Altura real 123
        avance 150cm            #segmento 7 Altura real 123
        gira 90 grados der      #segmento 7 Altura real 123 #s7 fin
        avance 150cm            #segmento 8 Altura real 123
        gira 90 grados der      #segmento 8 Altura real 123 #s8 fin
        suba 76cm               #segmento 9 Altura real 107
        avance 600cm            #segmento 9 Altura real 107
        gira 180 grados der     #segmento 9 Altura real 107 #s9 fin
        aterrizaje


        
        
        
    
    """

    sim_key = 'ce72f6b9-cd0d-473d-8eb2-26f4da75f5ea'
    # sim_key = None
    
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_up(97, 'cm')
        drone.fly_forward(150, 'cm')
        drone.yaw_left(90)

        drone.fly_forward(150, 'cm')
        drone.yaw_right(90)

        drone.fly_up(14, 'cm' )
        drone.fly_forward(150, 'cm' )
        drone.yaw_right(90)

        drone.fly_forward(150, 'cm' )
        drone.yaw_left(90)

        drone.fly_down(36, 'cm' )
        drone.fly_forward(150, 'cm')
        drone.yaw_left(90)

        drone.fly_forward(150, 'cm')
        drone.yaw_right(90)

        drone.fly_down(30, 'cm')
        drone.fly_forward(150, 'cm')
        drone.yaw_right(90)
        
        drone.fly_forward(150, 'cm')
        drone.yaw_right(90)


        drone.fly_up(76, 'cm')
        drone.fly_forward(600, 'cm')
        drone.yaw_right(180)

        drone.land()

        