import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to represent a single alion in the fleet. """

	def __init__(self, ai_game):
		""" Initialize the alien and set its starting position. """
		super().__init__()
		self.screen = ai_game.screen

		# Load the alien image and set its rect attribute.
		self.image = pygame.image.load("images/spaceship.bmp")
		self.rect = self.image.get_rect()

		# Store the alien's exact horizontal position.
		self.x = float(self.rect.x)

		