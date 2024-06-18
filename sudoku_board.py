from libs.boardlib.board import *
import utils
import math


class SudokuBoard(Board):
  def __init__(self, display_surface, board_dimension, background_color, lines_color):
    self.board_dimension = board_dimension
    super(SudokuBoard, self).__init__(display_surface, board_dimension, background_color, lines_color)

  def __draw_grid(self, color, lw):
    ### Draws a 3x3 grid on the DSURFACE
    # Draw vertical lines
    cell_width = self.WIDTH/self.BOARD_W
    #x_dimension = self.board_dimension[0]
    #y_dimension = self.board_dimension[1]
    for width in range(0, self.WIDTH, int(cell_width)):
      if width % 3 == 0: # For now just asume that the board should be divided in three
        lines_width = lw * 5 # Make the third and sixth line thicker

      else:
        lines_width = lw
      pygame.draw.line(self.DSURFACE, color, [width, 0], [width, self.HEIGHT], lines_width)

    # Draw horizontal lines
    cell_height = self.HEIGHT/self.BOARD_H
    for height in range(0, self.HEIGHT, int(cell_height)):
      if height % 3 == 0: # For now just asume that the board should be divided in three
        lines_width = lw * 5
      else:
        lines_width = lw
      pygame.draw.line(self.DSURFACE, color, [0, height], [self.WIDTH, height], lines_width)

  def get_box(self, box_number):
    box = []
  
    if box_number == 0:
      cell_pos = (0,0)
    elif box_number == 1:
      cell_pos = (0,3)
    elif box_number == 2:
      cell_pos = (0,6)
    elif box_number == 3:
      cell_pos = (3,0)
    elif box_number == 4:
      cell_pos = (3,3)
    elif box_number == 5:
      cell_pos = (3,6)
    elif box_number == 6:
      cell_pos = (6,0)
    elif box_number == 7:
      cell_pos = (6,3)
    elif box_number == 8:
      cell_pos = (6,6) 


    temp_row = []
    for i in range(cell_pos[0], cell_pos[0] + 3):
      for j in range(cell_pos[1], cell_pos[1] + 3):
        temp_row.append(self.board[i][j].id)
      box.append(temp_row)
      temp_row = []
    return box

  def update(self, events):
    self.DSURFACE.fill(self.background_color)
    self.__draw_grid(self.lines_color, 1)
    self.event_handling(events)

    ### Grid Update ###

    # Highlight the current selected cell, if any
    if self.current_cell_selected != None and self.highlight == True:
      self.highlight_cell(self.current_cell_selected)

    # Update sprites on grid
    self.sprite_group.draw(self.DSURFACE)