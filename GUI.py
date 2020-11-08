import pygame
from Search import Search_On_GUI

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)


class Grid_Square:
    def __init__(self, square: pygame.Rect, row, col):
        self.square = square
        self.color = WHITE
        self.row = row
        self.column = col


class GUI:
    def __init__(self, screen_width, grid):
        pygame.init()
        self.grid = grid
        self.BOX_WIDTH = screen_width / len(grid)
        self.MARGIN = 1
        self.SCREEN = pygame.display.set_mode([screen_width, screen_width])

        self.game_done = False
        self.default_squares = self.create_default_squares()
        self.current_squares = self.default_squares
        self.current_squares_map = {
            grid_square: grid_square for grid_square in self.current_squares}

    def create_default_squares(self):
        default_squares = []
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                square = Grid_Square(
                    pygame.Rect(
                        self.coordinates_for_new_square(row, column)),
                    row,
                    column)
                default_squares.append(square)
        return default_squares

    def update_square_color(self, square_to_update: Grid_Square, color):
        self.current_squares_map[square_to_update].color = color
        pygame.draw.rect(self.SCREEN, color, square_to_update.square)
        pygame.display.flip()

    def draw_squares(self):
        for grid_square in self.current_squares:
            pygame.draw.rect(self.SCREEN, grid_square.color,
                             grid_square.square)
        pygame.display.flip()

    def coordinates_for_new_square(self, row, column):
        coordinates = [(self.MARGIN + self.BOX_WIDTH) * column + self.MARGIN,
                       (self.MARGIN + self.BOX_WIDTH) * row + self.MARGIN,
                       self.BOX_WIDTH, self.BOX_WIDTH]
        return coordinates

    def main(self):
        left_click_occurred = False
        right_click_happened = False
        start_position = []
        end_position = []
        self.draw_squares()
        
        while not self.game_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_done = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_done = True
                    if event.key == pygame.K_s:
                        if left_click_occurred and right_click_happened:
                            Search_On_GUI(self).depth_first_search(start_position[0], start_position[1],
                                                                   end_position[0], end_position[1])

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for grid_square in self.current_squares:
                        if grid_square.square.collidepoint(pos):
                            if event.button == 1 and not left_click_occurred:
                                self.update_square_color(grid_square, GREEN)
                                start_position = [
                                    grid_square.row, grid_square.column]
                                left_click_occurred = True
                            elif event.button == 3 and not right_click_happened:
                                self.update_square_color(grid_square, ORANGE)
                                end_position = [
                                    grid_square.row, grid_square.column]
                                right_click_happened = True
        pygame.quit()

test_grid = [[None]*8 for i in range(8)]
gui = GUI(600, test_grid)
gui.main()