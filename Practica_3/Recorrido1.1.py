from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
import time

sim_key = None
x = 155

# Función auxiliar para ejecutar acciones con tiempo de espera
def safe_move(drone, action, *args, delay=0.5):
    action(*args)
    time.sleep(delay)

# Contexto de simulador
with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
    safe_move(drone, drone.get_battery)
    safe_move(drone, drone.takeoff)
    
    # Primera secuencia de movimientos
    safe_move(drone, drone.fly_up, 95, 'cm')
    safe_move(drone, drone.fly_forward, 150, 'cm')
    safe_move(drone, drone.yaw_left, 90)
    
    # Segunda secuencia de movimientos
    safe_move(drone, drone.fly_forward, x, 'cm')
    safe_move(drone, drone.yaw_right, 90)
    safe_move(drone, drone.fly_up, 44, 'cm')
    safe_move(drone, drone.fly_down, 20, 'cm')
    safe_move(drone, drone.fly_forward, 150, 'cm')
    safe_move(drone, drone.yaw_right, 90)
    
    # Tercera secuencia de movimientos
    safe_move(drone, drone.fly_forward, x, 'cm')
    safe_move(drone, drone.yaw_left, 90)
    safe_move(drone, drone.fly_down, 40, 'cm')
    safe_move(drone, drone.fly_forward, 150, 'cm')
    safe_move(drone, drone.yaw_left, 90)
    
    # Cuarta secuencia de movimientos
    safe_move(drone, drone.fly_forward, x, 'cm')
    safe_move(drone, drone.yaw_right, 90)
    safe_move(drone, drone.fly_down, 30, 'cm')
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
