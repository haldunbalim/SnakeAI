class State():
    _state_data_names = ["apple_snake_lateral_distance", "apple_snake_frontal_distance",
                         "snake_body_part_frontal_distance", "snake_body_part_left_distance",
                         "snake_body_part_right_distance", "wall_frontal_distance",
                         "wall_right_distance"]
    _width_offset = 100
    _top_offset = 50
    _line_inbetween_offset = 50
    _font = 12

    def __init__(self, canvas, data):
        self.data = data
        self.canvas = canvas
        self.texts = []

    def visualize(self, canvas_width):
        if len(self.texts) > 0:
            for text in self.texts:
                self.canvas.delete(text)

        for idx, data_line in enumerate(self.data):
            text = self.canvas.create_text(canvas_width + self._width_offset,
                                           self._top_offset + self._line_inbetween_offset * idx,
                                           text="{}: {}".format(self._state_data_names[idx], data_line),
                                           font=self._font)
            self.texts.append(text)