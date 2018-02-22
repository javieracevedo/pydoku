from libs.board import *


class SudokuBoard(Board):
  def __init__(self, display_surface, board_dimension, background_color, lines_color):
    super(SudokuBoard, self).__init__(display_surface, board_dimension, background_color, lines_color)

  def __draw_grid(self, color, lw):
    ### Draws a 3x3 grid on the DSURFACE
    # Draw vertical lines
    cell_width = self.WIDTH/self.BOARD_W
    for width in range(cell_width, self.WIDTH, cell_width):
      if width % 3 == 0:
        lines_width = lw * 5
      else:
        lines_width = lw
      pygame.draw.line(self.DSURFACE, color, [width, 0], [width, self.HEIGHT], lines_width)

    # Draw horizontal lines
    cell_height = self.HEIGHT/self.BOARD_H
    for height in range(cell_height, self.HEIGHT, cell_height):
      if height % 3 == 0:
        lines_width = lw * 5
      else:
        lines_width = lw
      pygame.draw.line(self.DSURFACE, color, [0, height], [self.WIDTH, height], lines_width)

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


    pygame.display.update()
