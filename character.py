import pygame

class Character:
	"""A class to manage a character"""

	def __init__(self, ai_game):
		"""Initialize the character and set its starting posittion."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		# Loading the image 
		self.image = pygame.image.load("images/astro.bmp")

		# Atributo rect
		self.rect = self.image.get_rect()

		# Posicionando al astronauta
		self.rect.bottomright = (675, self.screen.get_rect().height)


	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
