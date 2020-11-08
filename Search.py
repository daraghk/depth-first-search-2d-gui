import time

RED = (255, 0, 0)

class Search_On_GUI:
    def __init__(self, GUI):
        self.grid = GUI.grid
        self.GUI = GUI
        self.directions = [[0, 1], [1,0], [-1,0], [0, -1]]  # right, down, left, up
        self.goal_found = False

    def depth_first_search(self, row, col, target_row, target_col):
        if not self.goal_found:
            if row == target_row and col == target_col:
                self.grid[row][col] = 'Y'  # Found
                self.goal_found = True
                return

            self.grid[row][col] = 'X'  # Visited
            for square in self.GUI.current_squares:
                if square.row == row and square.column == col:
                    self.GUI.update_square_color(square, (255, 0, 0))
            time.sleep(0.075)

            for direction in self.directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if self.is_move_valid(new_row, new_col):
                    self.depth_first_search(
                        new_row, new_col, target_row, target_col)

    def is_move_valid(self, row, col):
        if row < 0 or row > len(self.grid) - 1:
            return False
        if col < 0 or col > len(self.grid[0]) - 1:
            return False
        if self.grid[row][col] == 'X':
            return False
        return True
