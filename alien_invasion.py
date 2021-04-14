import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		# Creando una instancia
		self.settings = Settings()

		# Una vez creada screen, utilizamos los atributos de Settings
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Se crea una  intancia de ship
		# Al agregarle self, Ship tiene acceso a la instancia de AlienInvation
		# y tiene acceso a todos los metodos de AlienInvacion. 
		self.ship = Ship(self)

		# Set the background color.
		# self.bg_color = (230, 230, 230)


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			# Antes ------------------------------
			# for event in pygame.event.get():
			# 	if event.type == pygame.QUIT:
			# 		sys.exit()
			self._check_events()
			self._update_screen()

		# Redraw the screen during each pass through the loop.
		# Agregando el color al fondo de pantalla con cada pasos
		# Utilizando los atributos de Settings para rellenar la pantalla
		# self.screen.fill(self.settings.bg_color) -- _update_screen

		# # Dibujando la nave en la pantalla, con el metodo blitme
		# self.ship.blitme() -- _update_screen

		# # Make the most recently drawn screen visible.
		# pygame.display.flip() -- _update_screen


	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		pygame.display.flip()


if __name__ == "__main__":
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()


