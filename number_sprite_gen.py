# Number Sprite Generator factory
import pygame


class NumberSpriteGen(object):
  def factory(number):
    if number == 1: return Number("sprites/one.png")
    if number == 2: return Number("sprites/two.png")
    if number == 3: return Number("sprites/three.png")
    if number == 4: return Number("sprites/four.png")
    if number == 5: return Number("sprites/five.png")
    if number == 6: return Number("sprites/six.png")
    if number == 7: return Number("sprites/seven.png")
    if number == 8: return Number("sprites/eight.png")
    if number == 9: return Number("sprites/nine.png")
    if number == 0: return Number("sprites/zero.png")

  factory = staticmethod(factory)

class Number(pygame.sprite.Sprite):
  def __init__(self, sprite_img):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load(sprite_img)
    self.rect = self.image.get_rect()



