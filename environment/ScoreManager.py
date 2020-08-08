from utils import Singleton

class ScoreManager(metaclass=Singleton):
    _initial_score = 20
    _increment = 10
    _min_apple_eat_score = 5

    def __init__(self):
        self.total_score = 0
        self.curr_apple_score = self._initial_score
        self.curr_apple_score_initial = self._initial_score

    def decrement_score(self):
        self.curr_apple_score = max(self._min_apple_eat_score, self.curr_apple_score - 1)

    def apple_eaten(self):
        self.total_score += self.curr_apple_score
        score_earned = self.curr_apple_score

        self.curr_apple_score_initial += self._increment
        self.curr_apple_score = self.curr_apple_score_initial

        return score_earned

    def __repr__(self):
        return "Total Score:{}".format(self.total_score)