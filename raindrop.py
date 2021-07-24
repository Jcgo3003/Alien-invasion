import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
	""" A class to represent rain """

	def __init__(self, ai_game):
		""" Initialize the rain and set its starting possition"""
		super().__init__()
		self.screen = ai_game.screen

		# Settings
		self.settings = ai_game.settings

		# Load the rain image and set its rect attribute.
		self.image = pygame.image.load("images/raindrop.bmp")
		self.rect = self.image.get_rect()

		# Store the rain position
		self.y = float(self.rect.y)

	def update(self):
		""" Let the rain falling down """
		self.y += self.settings.rain_speed 
		self.rect.y = self.y

	# def check_edges(self):
	# 	""" Return True if the rain gets to the bottom"""
	# 	screen_rect = self.screen.get_rect()

	# 	if self.rect.down >= screen_rect.down: 
	# 		return True
