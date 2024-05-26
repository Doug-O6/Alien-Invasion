import pygame

class Ship:
  """This class manages the ship functions."""

  def __init__(self, ai_game):
    """ Initialize the ship and set the starting position."""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    # Load the ship image and generate it's rectangle.
    self.image = pygame.image.load('images/ship.bmp').convert_alpha()
    self.rect = self.image.get_rect()

    # Set the position of each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom

    # Movement flag.
    self.move_right = False

  def update(self):
    """Update the ships position based on the status of the movement flag."""
    if self.move_right:
      self.rect.x += 1

  def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)


