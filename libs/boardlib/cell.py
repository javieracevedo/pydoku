# Javier Acevedo 2/25/2018
# Cell represents a space to store a sprite in my Board Library
import pygame

class Cell(object):
  def __init__(self, position, sprite, overwrite=False):
    self.position = position # Position inside board grid
    self.sprite = sprite
    if sprite:
      self.id = self.sprite.id # Set to 0 by default, meaning empty
    else:
      self.id = None
    self.overwrite = overwrite

  def __repr__(self):
    return "Cell Position: ({})\n".format(self.position)

  def empty(self):
    self.sprite = None
    self.id = None

  def isEmpty(self):
    if not self.sprite:
      return True
    return False