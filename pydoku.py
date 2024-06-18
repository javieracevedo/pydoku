import pygame
import libs.textinputlib.text_input as text_input
import sudoku_board as board
#from pydoku_sprites import *
from number_sprite_gen import *
import utils

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.font.init()
winner_font = pygame.font.SysFont("monospace", 30)
winner_font.set_bold(True)
restart_font = pygame.font.SysFont("monospace", 15)
restart_font.set_bold(True)

# Window and Grid properties
pygame.display.set_caption('Sudoku')
window_dimension = (640, 640)
DSURFACE = pygame.display.set_mode(window_dimension)
sudoku_board_dimensions = (9, 9)
background_color = (255, 255, 255)
grid_lines_color = (0, 0, 0)

# Sudoku board instance
sudoku_board = board.SudokuBoard(DSURFACE, sudoku_board_dimensions, background_color, grid_lines_color)
sudoku_board.init()

# Sudoku specific board settings
sudoku_board.scale_cell_sprite = False  # Do not scale sprites on this board
sudoku_board.highlight = True
sudoku_board.highlight_color = (255, 0, 0)
sudoku_board.highlight_color_alpha = 100

# Used to get text input in pygame, so we can input numbers in a given cells
textinput = text_input.TextInput()


def draw_win():
    # Shows the winner on the screen
    overlay = pygame.Surface(DSURFACE.get_size())
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    DSURFACE.blit(overlay, (0, 0))
    win_text = winner_font.render("YOU WIN", 1, WHITE)
    restart_text = restart_font.render("Press (Space) to restart", 1, RED)

    DSURFACE.blit(win_text, ((window_dimension[0] * 0.5) - win_text.get_width() * 0.5,
                             (window_dimension[1] * 0.5) - win_text.get_height() * 0.5))
    DSURFACE.blit(restart_text, ((window_dimension[0] * 0.5) - restart_text.get_width() * 0.5,
                                 (window_dimension[1]) * 0.6))
    # pygame.display.flip()


def select_board_cell(mouse_pos):
    sudoku_board.select_cell(mouse_pos)


def populate_board():
    """
    Reads a file with a sudoku board and inserts every value in the sudoku_board
    Note: For now, assumes its a 9x9 board, always
    """
    print("pydoku:populate_board -- Populating Board")

    lines = []

    sudoku_board_path = "boards/sudoku_board_0.txt"
    # Read sudokuboards file and store the lines in a list
    with open(sudoku_board_path) as f_in:
        for line in utils.nonblank_lines(f_in):
            lines.append(line)

    # Iterate over lines list and insert the corresponding values in the board
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            cell = (x, y)
            if lines[x][y] != "0":
                number = NumberSpriteGen.factory(int(lines[x][y]))
                # Set the third argument to false, so the initial board values
                # cannot be modified
                sudoku_board.insert(number, cell, False)


def check_row(row):
    for c in row:
        if utils.appearsTwice(row, c, "0"):
            print("Uh oh! : {} repeated more than twice in row {}".format(c, row))
            return False
    return True


def check_col(col):
    for k in col:
        if utils.appearsTwice(col, k, "0"):
            print("Uh oh! : {} repeated more than twice in col {}".format(k, col))
            return False
    return True


def check_boxes(sudoku_board):
    board = sudoku_board.board
    arr_box = None
    for i in range(len(board)):
        arr_box = sudoku_board.get_box(i)
        for arr in arr_box:
            for v in arr:
                appearance = utils.appearsTwice(arr_box, v)
                if appearance:
                    return True
    return False


def sudoku_check(sudoku_board):
    row, col = ("", "")

    board_len = len(sudoku_board.board)
    filled = sudoku_board.filled()

    # If board is full, check if there are any errors
    if filled:
        # TODO: Im not particularly proud of this solution, I intend to fix this uglyness
        # on the next version of my Board library.

        # Check rows and columns (convert this to a function)
        for i in range(board_len):

            # Get row_columns string
            for j in range(board_len):
                current_cell_value = sudoku_board.board[i][j].id
                row += str(sudoku_board.board[i][j].id)
                col += str(sudoku_board.board[j][i].id)

            if not check_row(row):
                return False

            if not check_col(col):
                return False

            # Empty the strings, for every row and col
            row, col = ("", "")
        return True


# Read a sudoku board from text and insert it on the sudoku board
populate_board()

# Grid events registrations
sudoku_board.register_event(select_board_cell, "on_cell_lmb_down")

# sudoku_board.get_box(0)
# check_win = sudoku_check(sudoku_board)
print(sudoku_board.get_box(5))
if check_boxes(sudoku_board):
    print("MMMG")

running = True
while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update events in both sudoku_board and textinput instances
    sudoku_board.update(events)
    textinput.update(events)

    # Get input from the keyboard
    current_input = textinput.get_text()

    # Check if there is any cell selected on the grid
    if sudoku_board.current_cell_selected is not None:
        # Check if the current input value is any number between 1 and 9, if it's
        # any of those generate a sprite for that number and insert the sprite in
        # the grid
        for i in range(1, 10):
            if current_input == str(i):
                number = NumberSpriteGen.factory(int(current_input))
                sudoku_board.insert(number, sudoku_board.current_cell_selected, str(i))

        textinput.clear_text()

    # check_win = sudoku_check(sudoku_board)
    check_win = False
    if check_win:
        draw_win()

    pygame.display.update()
