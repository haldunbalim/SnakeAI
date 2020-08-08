from controllers import ManualController
from environment import Environment
from simulation import Simulator

if __name__ == "__main__":
    controller = ManualController()
    game_simulator = Environment(controller)
    game_simulator.make(True)
    snake_history, apple_history, score_history, state_history = game_simulator.simulate(printing=True, logging=True)
    simulator = Simulator(snake_history, apple_history, score_history, state_history, manual=True)
    simulator.start()