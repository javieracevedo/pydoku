import pygame
import libs.text_input as text_input
#import libs.board as board
import sudoku_board as board
from pydoku_sprites import *
from number_sprite_gen import *


# Window and Grid properties
DSURFACE = pygame.display.set_mode((640, 640))
sudoku_board_dimensions = (9,9)
background_color = (255,255,255)
grid_lines_color = (0,0,0)


# Sudoku board instance
sudoku_board = board.SudokuBoard(DSURFACE, sudoku_board_dimensions, background_color, grid_lines_color)

# Sudoku specific board settings
sudoku_board.scale_cell_sprite = False # Do not scale sprites on this board
sudoku_board.highlight = True
sudoku_board.highlight_color = (255,0,0)
sudoku_board.highlight_color_alpha = 100

# Used to get text input in pygame, so we can input numbers in a given cells
textinput = text_input.TextInput()


def select_board_cell(mouse_pos):
  sudoku_board.select_cell(mouse_pos)


def populate_board():
  sudoku_board_file = open("boards/sudokuboards.txt")
  sudoku_board_file = sudoku_board_file.readlines()
  for i in range(len(sudoku_board_file)):
    for j in range(len(sudoku_board_file[i]) - 1):
      #print "{}, {}".format(i,j)
      cell = (i,j)
      #sudoku_board.board[i][j] = sudoku_board_file[i][j]
      print "populate: {}".format(cell)
      if sudoku_board_file[i][j] != "0":
        number = NumberSpriteGen.factory(int(sudoku_board_file[i][j]))
        sudoku_board.insert_sprite(number, cell, str(i))


# Read a sudoku board from text and insert it on the sudoku board
populate_board()


# Grid events registrations
sudoku_board.register_event(select_board_cell, "on_cell_lmb_down")

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

  # Check if there is any cell seleected on the grid
  if sudoku_board.current_cell_selected != None:
    # Check if the current input value is any number between 1 and 9, if it's
    # any of those generate a sprite for that number and insert the sprite in
    # the grid
    for i in xrange(1,10):
      if current_input == str(i):
        number = NumberSpriteGen.factory(int(current_input))
        sudoku_board.insert_sprite(number, sudoku_board.current_cell_selected, str(i))

    textinput.clear_text()

  pygame.display.update()
