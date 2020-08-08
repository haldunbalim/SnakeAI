from environment import SnakeModel
from environment import Direction
from environment import Action

class ManualController():
    def __init__(self):
        pass

    def decide_next_action(self):
        while True:
            key = input()
            if key.lower() not in ["w", "a", "s", "d", ""]:
                print("{} is not a valid key".format(key))
            else:
                snake_dir = SnakeModel().direction
                if key.lower() == "":
                    return Action.KEEP

                if key.lower() == "w":
                    if snake_dir is Direction.NORTH or snake_dir is Direction.SOUTH:
                        return Action.KEEP
                    elif snake_dir is Direction.WEST:
                        return Action.TURN_RIGHT
                    else:
                        return Action.TURN_LEFT

                if key.lower() == "s":
                    if snake_dir is Direction.NORTH or snake_dir is Direction.SOUTH:
                        return Action.KEEP
                    elif snake_dir is Direction.WEST:
                        return Action.TURN_LEFT
                    else:
                        return Action.TURN_RIGHT

                if key.lower() == "a":
                    if snake_dir is Direction.EAST or snake_dir is Direction.WEST:
                        return Action.KEEP
                    elif snake_dir is Direction.NORTH:
                        return Action.TURN_LEFT
                    else:
                        return Action.TURN_RIGHT

                if key.lower() == "d":
                    if snake_dir is Direction.EAST or snake_dir is Direction.WEST:
                        return Action.KEEP
                    elif snake_dir is Direction.NORTH:
                        return Action.TURN_RIGHT
                    else:
                        return Action.TURN_LEFT
