import sys
import pygame
from settings import Settings
from ship import Ship
from character import Character
from bullet import Bullet

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		# Creando una instancia
		self.settings = Settings()

		# Adding some fullscreen settings
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		# Una vez creada screen, utilizamos los atributos de Settings
		# self.screen = pygame.display.set_mode(
		# 	(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# Se crea una  intancia de ship
		# Al agregarle self, Ship tiene acceso a la instancia de AlienInvation
		# y tiene acceso a todos los metodos de AlienInvacion. 
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.character = Character(self)

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
			#Adding movement updates
			self.ship.update()
			self.bullets.update()

			# Get rid of bullets that have disappered
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <= 0:
					self.bullets.remove(bullet)
			# print(len(self.bullets))


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

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			# #Adding key events
			# elif event.type == pygame.KEYDOWN:	
			# 	if event.key == pygame.K_RIGHT:
			# 		# move the ship to the right.
			# 		# self.ship.rect.x += 1
			# 		self.ship.moving_right = True
			# 	elif event.key == pygame.K_LEFT:
			# 		self.ship.moving_left = True


			# elif event.type == pygame.KEYUP:
			# 	if event.key == pygame.K_RIGHT:
			# 		self.ship.moving_right = False
			# 	elif event.key == pygame.K_LEFT:
			# 		self.ship.moving_left = False

	def _check_keydown_events(self, event):
		""" Respond to keypresses"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True

		# Quiting with q
		elif event.key == pygame.K_q:
			sys.exit()

		# Shoting
		elif event.key == pygame.K_SPACE:		
			self._fire_bullet()


	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def _fire_bullet(self):
		""" Create a new bullet and add it to the bullets group. """
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()


		self.character.blitme()

		pygame.display.flip()



if __name__ == "__main__":
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()