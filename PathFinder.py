import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = "comicsans"

class SearchOnGUI:
    def __init__(self, GUI):
        self.grid = GUI.grid
        self.GUI = GUI

    def depth_first_search(self, row, col, target):
        if self.grid[row][col] == target:
            self.grid[row][col] = 'Y'
            self.GUI.write_underlying_grid_to_screen()
            return

        self.grid[row][col] = 'X'  # mark element as visited
        self.GUI.write_underlying_grid_to_screen()
        time.sleep(0.1)

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

class Gui:
    def __init__(self, window_side_length, grid):
        self.grid = grid
        self.BOX_WIDTH = window_side_length / len(grid)
        self.WINDOW_SIZE = [window_side_length, window_side_length]
        self.MARGIN = 1
        pygame.init()
        self.FONT = pygame.font.SysFont(FONT, 40)
        self.SCREEN = pygame.display.set_mode(self.WINDOW_SIZE)
        self.game_done = False
        self.default_rectangles = self.default_rectangles()
        self.current_rectangles = self.default_rectangles

    def default_rectangles(self):
        default_rectangles = []
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                rect = pygame.Rect(self.coordinates_for_new_rectangle(row, column))
                default_rectangles.append(rect)
        return default_rectangles

    def clear_screen_text(self):
        for rect in self.current_rectangles:
            pygame.draw.rect(self.SCREEN, WHITE, rect)
        pygame.display.flip()

    def write_underlying_grid_to_screen(self):
        self.clear_screen_text()
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                text = self.FONT.render(str(self.grid[row][column]), 1, BLACK)
                self.SCREEN.blit(text, self.position_to_write_text(row, column, text))
        pygame.display.flip()

    def coordinates_for_new_rectangle(self, row, column):
        coordinates = [(self.MARGIN + self.BOX_WIDTH) * column + self.MARGIN,
                       (self.MARGIN + self.BOX_WIDTH) * row + self.MARGIN,
                       self.BOX_WIDTH, self.BOX_WIDTH]
        return coordinates

    def position_to_write_text(self, row, column, text):
        positions = self.BOX_WIDTH * column - text.get_width() // 2 + self.BOX_WIDTH // 2, \
                    self.BOX_WIDTH * row - text.get_height() // 2 + self.BOX_WIDTH // 2
        return positions

    def main(self):
        while not self.game_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_done = True
                    if event.key == pygame.K_RETURN:
                        self.clear_screen_text()
                        self.write_underlying_grid_to_screen()
                    if event.key == pygame.K_s:
                        SearchOnGUI(self).depth_first_search(3, 4, 310)
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for rect in self.rectangles:
                        if rect.collidepoint(pos):
                            print(rect)
        pygame.quit()

test_grid = [[1, 2, 3, 10, 99],
          [4, 5, 6, 3, 99],
          [5, 34, 6, 7, 99],
          [56, 67, 34, 90, 99],
          [100, 34, 67, 310, 99]]

gui = Gui(600, test_grid)
gui.main()


#fix gridlines and write positions
#accept input grid search position