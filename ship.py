import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		# Se asigna el atributo screen a ship
		self.screen = ai_game.screen
		# Settings para la velocidad para poder utilizarlo en update()
		self.settings =ai_game.settings

		# Para colocar la nave en la pantalla
		self.screen_rect = ai_game.screen.get_rect()

		# Lead the ship image and get its rect.
		# Cargando la imagen de ship
		self.image = pygame.image.load("images/ship.bmp") 
		# Con la image cargada, llamamos a get_rect para acceder
		# Al atributo rect para pocisionar la nave.
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom center of the screen.
		# Pocisionando la nave al fondo en medio de la pantalla.
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)

		# Movement flag
		self.moving_right = False
		self.moving_left = False


	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right:
		# if self.moving_right:
			# self.rect.x += 1
			self.x += self.settings.ship_speed
			
		if self.moving_left and self.rect.left > 0:
		# if self.moving_left:
			# self.rect.x -= 1
			self.x -= self.settings.ship_speed

		# Update rect object from self.x
		self.rect.x = self.x


	def blitme(self):
		"""Draw the ship at its currest locacion."""
		# El metodo blit dibuja la nave en la posicion especifica
		# Por eso toma como parametros la imagen y su rectangulo con rect
		self.screen.blit(self.image, self.rect)

# Pygame trata a todos los elementos como rectangulos, por eso rect
# Aqui se esta tratando a la nave y a la pantalla como rectangulos
# 