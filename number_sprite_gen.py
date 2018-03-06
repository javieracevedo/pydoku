# Number Sprite Generator factory
import pygame


class NumberSpriteGen(object):
  def factory(number):
    if number == 1: return Number("sprites/one.png", "1")
    if number == 2: return Number("sprites/two.png", "2")
    if number == 3: return Number("sprites/three.png", "3")
    if number == 4: return Number("sprites/four.png", "4")
    if number == 5: return Number("sprites/five.png", "5")
    if number == 6: return Number("sprites/six.png", "6")
    if number == 7: return Number("sprites/seven.png", "7")
    if number == 8: return Number("sprites/eight.png", "8")
    if number == 9: return Number("sprites/nine.png", "9")
    if number == 0: return Number("sprites/zero.png", "0")

  factory = staticmethod(factory)

class Number(pygame.sprite.Sprite):
  def __init__(self, sprite_img, sid):
    pygame.sprite.Sprite.__init__(self)

    self.image = pygame.image.load(sprite_img)
    self.rect = self.image.get_rect()
    self.id = sid


