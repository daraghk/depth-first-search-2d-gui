import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = "comicsans"

class Gui:
    def __init__(self, window_side_length, grid):
        self.grid = grid
        self.box_width = window_side_length / len(grid)
        self.window_size = [window_side_length, window_side_length]
        self.margin = 1
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        self.game_done = False
        self.font = pygame.font.SysFont(FONT, 40)

    def draw_original_grid(self):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                pygame.draw.rect(self.screen, WHITE, self.get_coordinates(row, column))
                text = self.font.render(str(self.grid[row][column]), 1, BLACK)
                self.screen.blit(text, self.write_position(row, column, text))
        pygame.display.flip()

    def update_grid_position_on_screen(self, row_to_change, column_to_change, update_value):
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                pygame.draw.rect(self.screen, WHITE, self.get_coordinates(row, column))
                if row == row_to_change and column == column_to_change:
                    text = self.font.render(update_value, 1, BLACK)
                    self.screen.blit(text, self.write_position(row_to_change, column_to_change, text))
                else:
                    text = self.font.render(str(self.grid[row][column]), 1, BLACK)
                    self.screen.blit(text, self.write_position(row, column, text))
        pygame.display.flip()

    def get_coordinates(self, row, column):
        coordinates = [(self.margin + self.box_width) * column + self.margin,
                       (self.margin + self.box_width) * row + self.margin,
                       self.box_width, self.box_width]
        return coordinates

    def write_position(self, row, column, text):
        positions = self.box_width * column - text.get_width() // 2 + self.box_width // 2, \
                    self.box_width * row - text.get_height() // 2 + self.box_width // 2
        return positions

    def depth_first_search(self, row, col, target):
        if self.grid[row][col] == target:
            self.update_grid_position_on_screen(row, col, 'Y')
            return

        self.grid[row][col] = 'X'  # mark element as visited
        self.update_grid_position_on_screen(row, col, 'X')
        time.sleep(0.5)

        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # right, up, left, down
        for dir in directions:
            new_row = row + dir[0]
            new_col = col + dir[1]
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

    def main(self):
        while not self.game_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_done = True
            self.draw_original_grid()
            time.sleep(5)
            self.depth_first_search(1, 1, 310)
            time.sleep(100)
        pygame.quit()


grid_t = [[1, 2, 3, 10, 99], [4, 5, 6, 3, 99], [5, 34, 6, 7, 99], [56, 67, 34, 90, 99], [100, 34, 67, 310, 99]]
gui = Gui(600, grid_t)
gui.main()


#fix gridlines and write positions
#accept input grid search position