import pygame

class Ship:
  """This class manages the ship functions."""

  def __init__(self, ai_game):
    """ Initialize the ship and set the starting position."""
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.screen_rect = ai_game.screen.get_rect()

    # Load the ship image and generate it's rectangle.
    self.image = pygame.image.load('images/ship.bmp').convert_alpha()
    self.rect = self.image.get_rect()

    # Start each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom

    # Store a decimal value for the ships's horizontal position.
    self.x = float(self.rect.x)

    # Movement flag.
    self.move_right = False
    self.move_left = False

  def update(self):
    """Update the ships position based on the status of the movement flag."""
    # Update the ship's x value, not the rect value.
    if self.move_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    if self.move_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed

    # Update rect object from self.x
    self.rect.x = self.x

  def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)


