from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    # sim_key = 'ee3d9de3-3f0d-4c0f-bcff-64b458927e3b'
    sim_key = None
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_up(20, 'cm')
        drone.fly_forward(distance, 'cm')
        drone.fly_left(distance, 'cm')
        drone.fly_to_xyz(10, 20, 30, 'in')
        drone.fly_curve(25, 25, 0, 0, 50, 0, 'cm')
        drone.fly_backward(distance, 'cm')
        drone.fly_right(distance, 'cm')
        # drone.flip_backward()

        drone.land()