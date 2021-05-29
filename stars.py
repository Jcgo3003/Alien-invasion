import pygame
from pygame.sprite import Sprite


class Stars(Sprite):
	""" A class to grind stars all over the sky """

	def __init__(self, ai_game):
		""" Initialize the stars """
		super().__init__()
		self.screen = ai_game.screen

		# Load stars 
		self.image = pygame.image.load("images/star.bmp")
		self.rect = self.image.get_rect()

		# Store the stars exact position
		self.x = float(self.rect.x)



