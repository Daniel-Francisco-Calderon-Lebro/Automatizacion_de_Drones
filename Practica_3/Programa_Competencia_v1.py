from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
import time

sim_key = None
x = 150
y = 150

# Función auxiliar para ejecutar acciones con tiempo de espera
def safe_move(drone, action, *args, delay=0.5):
    action(*args)
    time.sleep(delay)
    # Alturas:
    #     Obstaculo #1 155 centimetros de base y diametro interior 40cm verde     155+20=175
    #     Obstaculo #2 176 centimetros de base y diametro interior 27cm rojo      176+13=199
    #     Obstaculo #3 137 centimetros de base y diametro interior 32cm blanco    137+16=156
    #     Obstaculo #4 107 centimetros de base y diametro interior 32cm amarillo  107+16=123
    
# Contexto de simulador
with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
    safe_move(drone, drone.get_battery)
    safe_move(drone, drone.takeoff)
    
    # Primera secuencia de movimientos
    safe_move(drone, drone.fly_up, 43, 'cm')
    safe_move(drone, drone.fly_forward, 150, 'cm')
    safe_move(drone, drone.yaw_left, 90)
    
    # Segunda secuencia de movimientos
    safe_move(drone, drone.fly_forward, x + 5, 'cm')
    safe_move(drone, drone.yaw_right, 90)

    # # safe_move(drone, drone.fly_up, 44, 'cm')
    safe_move(drone, drone.fly_up, 76, 'cm')
    
    safe_move(drone, drone.fly_forward, 150, 'cm')
    safe_move(drone, drone.yaw_right, 90)


    # Tercera secuencia de movimientos
    safe_move(drone, drone.fly_forward, x, 'cm')
    safe_move(drone, drone.yaw_left, 90)
    safe_move(drone, drone.fly_down, 43, 'cm')
    safe_move(drone, drone.fly_forward, y, 'cm')
    safe_move(drone, drone.yaw_left, 90)
    
    # Cuarta secuencia de movimientos
    safe_move(drone, drone.fly_forward, x, 'cm')
    safe_move(drone, drone.yaw_right, 90)
    safe_move(drone, drone.fly_up, 20, 'cm')
    safe_move(drone, drone.fly_forward, 150, 'cm')
    safe_move(drone, drone.yaw_right, 90)
    
    # Quinta secuencia de movimientos
    safe_move(drone, drone.fly_forward, x, 'cm')
    safe_move(drone, drone.yaw_right, 90)
    
    # Última secuencia de movimientos
    safe_move(drone, drone.fly_up, 106, 'cm')
    safe_move(drone, drone.fly_forward, 500, 'cm')
    safe_move(drone, drone.fly_forward, 100, 'cm')
    safe_move(drone, drone.yaw_right, 180)
    
    # Aterrizaje
    safe_move(drone, drone.land)
