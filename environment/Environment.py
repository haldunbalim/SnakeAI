from .GridModel import GridModel
from .SnakeModel import SnakeModel
from .AppleModel import AppleModel
from .Sensor import Sensor
from .ScoreManager import ScoreManager


class Environment():
    def __init__(self, controller):
        self.time_step = 0
        self.controller = controller
        self.grid_model = GridModel()
        self.snake_model = SnakeModel()
        self.apple_model = AppleModel()
        self.sensor = Sensor()
        self.snake_history = []
        self.apple_history = []
        self.score_history = []
        self.state_history = []
        self.first = True

    def make(self, printing):
        self.first = True
        return self.sensor.get_state(self.snake_model, self.apple_model)

    def step(self, action, logging, printing):
        reward = 0
        if not self.first:
            next_direction = self.snake_model.direction.find_next_direction(action)
            self.snake_model.direction = next_direction
            new_head = self.snake_model.move()

            self.snake_model.body.appendleft(new_head)

            # order with the line above means if the snake eats its last part of tail when it moves on it
            # seems like a design choice
            if new_head != self.apple_model.pos:
                # didnt ate apple shrink snake
                self.snake_model.body.pop()
                ScoreManager().decrement_score()
            else:
                # ate apple dont shrink
                # find new place for apple
                self.apple_model.find_place()
                reward = ScoreManager().apple_eaten()

            self.time_step += 1
        else:
            self.first = False

        state = self.sensor.get_state(self.snake_model, self.apple_model)
        if logging:
            self.log(state)
        if printing:
            self.print_current_log()

        return state, reward

    def print_current_log(self):
        print("Time step {}".format(self.time_step))
        print("Snake Pos: {}".format(self.snake_model.body))
        print("Apple Pos: {}".format(self.apple_model.pos))
        print(ScoreManager())

    def log(self, state):
        self.snake_history.append(list(self.snake_model.body.copy()))
        self.apple_history.append(self.apple_model.pos)
        self.score_history.append(ScoreManager().total_score)
        self.state_history.append(state)

    def get_log(self):
        return self.snake_history, self.apple_history, self.score_history, self.state_history

    def simulate(self, logging=False, printing=False):
        direction = None
        self.step(None, logging, printing)
        while True:
            action = self.controller.decide_next_action()
            state, action = self.step(action, logging, printing)
            if self.check_for_game_over():
                print("Game Over")
                break
        if logging:
            return self.get_log()

    def check_for_game_over(self):
        # snake ate itself
        head = self.snake_model.body[0]
        for body_part_idx in range(1, len(self.snake_model.body)):
            body_part = self.snake_model.body[body_part_idx]
            if head == body_part:
                return True
        if head[0] < 0 or head[0] >= GridModel()._num_squares_in_row:
            return True
        if head[1] < 0 or head[1] >= GridModel()._num_squares_in_col:
            return True
        return False
