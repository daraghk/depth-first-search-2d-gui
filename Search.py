import time

class SearchOnGUI:
    def __init__(self, GUI):
        self.grid = GUI.grid
        self.GUI = GUI
        self.directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # right, up, left, down

    def depth_first_search(self, row, col, target):
        if self.grid[row][col] == target:
            self.grid[row][col] = 'Y' # Found
            self.GUI.write_underlying_grid_to_screen()
            return

        self.grid[row][col] = 'X'  # Visited
        self.GUI.write_underlying_grid_to_screen()
        time.sleep(0.1)

        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if self.is_move_valid(new_row, new_col):
                return self.depth_first_search(new_row, new_col, target)

    def is_move_valid(self, row, col):
        if row < 0 or row > len(self.grid) - 1:
            return False
        if col < 0 or col > len(self.grid[0]) - 1:
            return False
        if self.grid[row][col] == 'X':
            return False
        return True
