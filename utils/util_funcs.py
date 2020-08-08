def get_num_squares_in_row_col():
    num_squares_in_row = None
    num_squares_in_col = None
    with open("grid_config.txt","r") as file:
        lines = [line.split(": ") for line in file.readlines()]
        for var,val in lines:
            if var == "num_squares_in_row":
                num_squares_in_row = int(val)
            if var == "num_squares_in_col":
                num_squares_in_col = int(val)
    if num_squares_in_row is None or num_squares_in_col is None:
        raise Exception("Check format of grid_config.txt")
    return num_squares_in_row, num_squares_in_col