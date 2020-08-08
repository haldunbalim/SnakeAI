from utils import Singleton
from . import GridModel
from . import Direction

class Sensor(metaclass=Singleton):
    def __init__(self):
        pass

    # if lateral dist > 0 turn right
    # if frontal dist > 0 keep
    # orientation does not matter but changes right side
    def get_state(self, snake, apple):
        head_x, head_y = snake.body[0]
        direction = snake.direction
        apple_x, apple_y = apple.pos

        num_squares_in_row = GridModel()._num_squares_in_row
        num_squares_in_col = GridModel()._num_squares_in_col

        if direction is Direction.NORTH:
            apple_snake_lateral_distance = apple_x - head_x
            apple_snake_frontal_distance = head_y - apple_y

            snake_body_part_frontal_distance = num_squares_in_col
            snake_body_part_left_distance = num_squares_in_row
            snake_body_part_right_distance = num_squares_in_row

            for body_part_idx in range(1, len(snake.body)):
                body_part_x, body_part_y = snake.body[body_part_idx]
                if body_part_y == head_y:
                    if body_part_x > head_x:
                        snake_body_part_right_distance = min(snake_body_part_right_distance, body_part_x - head_x)
                    else:
                        snake_body_part_left_distance = min(snake_body_part_left_distance, head_x - body_part_x)
                if body_part_x == head_x:
                    if body_part_y < head_y:
                        snake_body_part_frontal_distance = min(snake_body_part_frontal_distance, head_y - body_part_y)

            wall_frontal_distance = head_y
            wall_right_distance = num_squares_in_row - head_x

        if direction is Direction.SOUTH:
            apple_snake_lateral_distance = head_x - apple_x
            apple_snake_frontal_distance = apple_y - head_y

            snake_body_part_frontal_distance = num_squares_in_col
            snake_body_part_left_distance = num_squares_in_row
            snake_body_part_right_distance = num_squares_in_row

            for body_part_idx in range(1, len(snake.body)):
                body_part_x, body_part_y = snake.body[body_part_idx]
                if body_part_y == head_y:
                    if body_part_x > head_x:
                        snake_body_part_right_distance = min(snake_body_part_right_distance, body_part_x - head_x)
                    else:
                        snake_body_part_left_distance = min(snake_body_part_left_distance, head_x - body_part_x)
                if body_part_x == head_x:
                    if body_part_y > head_y:
                        snake_body_part_frontal_distance = min(snake_body_part_frontal_distance, body_part_y - head_y)

            wall_frontal_distance = num_squares_in_col - head_y
            wall_right_distance = head_x

        if direction is Direction.EAST:
            apple_snake_lateral_distance = apple_y - head_y
            apple_snake_frontal_distance = apple_x - head_x

            snake_body_part_frontal_distance = num_squares_in_row
            snake_body_part_left_distance = num_squares_in_col
            snake_body_part_right_distance = num_squares_in_col

            for body_part_idx in range(1, len(snake.body)):
                body_part_x, body_part_y = snake.body[body_part_idx]
                if body_part_y == head_y:
                    if body_part_x > head_x:
                        snake_body_part_frontal_distance = min(snake_body_part_frontal_distance, body_part_x - head_x)
                if body_part_x == head_x:
                    if body_part_y > head_y:
                        snake_body_part_right_distance = min(snake_body_part_right_distance, body_part_y - head_y)
                    else:
                        snake_body_part_left_distance = min(snake_body_part_left_distance, head_y - body_part_y)

            wall_frontal_distance = num_squares_in_row - head_x
            wall_right_distance = num_squares_in_col - head_y

        if direction is Direction.WEST:
            apple_snake_lateral_distance = head_y - apple_y
            apple_snake_frontal_distance = head_x - apple_x

            snake_body_part_frontal_distance = num_squares_in_row
            snake_body_part_left_distance = num_squares_in_col
            snake_body_part_right_distance = num_squares_in_col

            for body_part_idx in range(1, len(snake.body)):
                body_part_x, body_part_y = snake.body[body_part_idx]
                if body_part_y == head_y:
                    if body_part_x < head_x:
                        snake_body_part_frontal_distance = min(snake_body_part_frontal_distance, head_x - body_part_x)
                if body_part_x == head_x:
                    if body_part_y < head_y:
                        snake_body_part_right_distance = min(snake_body_part_right_distance, head_y - body_part_y)
                    else:
                        snake_body_part_left_distance = min(snake_body_part_left_distance, body_part_y - head_y)

            wall_frontal_distance = head_x
            wall_right_distance = head_y

        return (apple_snake_lateral_distance, apple_snake_frontal_distance,
                snake_body_part_frontal_distance, snake_body_part_left_distance,
                snake_body_part_right_distance, wall_frontal_distance,
                wall_right_distance)