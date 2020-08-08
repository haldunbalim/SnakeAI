from enum import Enum
from .Action import Action

class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    # must reorient sensors according to current moving directions
    def find_next_direction(self, next_action):
        if next_action is Action.KEEP:
            return self
        if self is Direction.NORTH:
            if next_action is Action.TURN_LEFT:
                return Direction.WEST
            else:
                return Direction.EAST
        elif self is Direction.SOUTH:
            if next_action is Action.TURN_LEFT:
                return Direction.EAST
            else:
                return Direction.WEST
        elif self is Direction.WEST:
            if next_action is Action.TURN_LEFT:
                return Direction.SOUTH
            else:
                return Direction.NORTH
        elif self is Direction.EAST:
            if next_action is Action.TURN_LEFT:
                return Direction.NORTH
            else:
                return Direction.SOUTH