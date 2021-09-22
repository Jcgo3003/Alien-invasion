import pygame.font

class Button:

	def __init__(self, ai_game, msg):
		""" Initialize button attributes """
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button message needs to prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		""" Turn msg into a rendered image and center text on the button """
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def draw_button(self): 
		""" Draw blank button and then draw message. """
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)


class Level_Buttons:
	""" A Class for drawing and displaying level buttons """
	def __init__(self, ai_game):
		""" Initialize button attributes """
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		# Setting dimensions and font
		self.width, self.height = 200, 40
		self.font = pygame.font.SysFont(None, 30)

		# Colors and text color 
		self.button_color_easy = (0, 150, 0) # Green for easy
		self.button_color_medium = (0, 0, 255) # Blue for medium 
		self.button_color_hard = (255, 0, 0) # Red for hard
		self.text_color = (255, 255, 255) # White for the text color

		# Build the button's rect object 
		self.x, self.y = self.screen_rect.center

		# Setting the buttons in exe Y
		pos_easy = self.y + 100
		pos_medium = self.y + 150
		pos_hard = self.y + 200

		# Building the objects
		self.rect_easy = pygame.Rect(0, 0, self.width, self.height)
		self.rect_easy.center = (self.x, pos_easy)
		
		self.rect_medium = pygame.Rect(self.x, pos_medium, self.width, self.height)
		self.rect_medium.center = (self.x, pos_medium)
		
		self.rect_hard = pygame.Rect(self.x, pos_hard, self.width, self.height)
		self.rect_hard.center = (self.x, pos_hard)

		# Setting all level buttons in y
		self._easy_button(pos_easy)
		self._medium_button(pos_medium)
		self._hard_button(pos_hard)


	def _easy_button(self, pos_easy):
		""" Turn msg into a rendered image and center text on the button """
		self.image_easy = self.font.render("Easy", True, self.text_color, self.button_color_easy)
		self.image_easy_rect = self.image_easy.get_rect()
		self.image_easy_rect.center = (self.x, pos_easy)	


	def _medium_button(self, pos_medium):
		""" Turn msg into a rendered image and center text on the button """
		self.image_medium = self.font.render("Medium", True, self.text_color, self.button_color_medium)
		self.image_medium_rect = self.image_medium.get_rect()
		self.image_medium_rect.center = (self.x, pos_medium)

	def _hard_button(self, pos_hard):
		""" Turn msg into a rendered image and center text on the button """
		self.image_hard = self.font.render("Hard", True, self.text_color, self.button_color_hard)
		self.image_hard_rect = self.image_hard.get_rect()
		self.image_hard_rect.center = (self.x, pos_hard)

	def draw_level_buttons(self):
		""" Drawing the level buttons """	
		self.screen.fill(self.button_color_easy, self.rect_easy)
		self.screen.blit(self.image_easy, self.image_easy_rect)

		self.screen.fill(self.button_color_medium, self.rect_medium)
		self.screen.blit(self.image_medium, self.image_medium_rect)

		self.screen.fill(self.button_color_hard, self.rect_hard)
		self.screen.blit(self.image_hard, self.image_hard_rect)


''' Notas
Por alguna razon los botones estan desalineados con el centro y pero el texto esta correctamente alineado con el centro, aunque solo en el eje x,
en el eje y, esta mucho mas arriva de lo normall

	


	# Build the button's rect object and center it.


		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.x, self.y = self.screen_rect.center

		self.rect.center = self.x - 300, self.y 

		Aqui estoy centrando el boton, Tambien aqui puedo cambiar donde va estar situado el objeto
	
self.rect_easy <rect(960, 490, 200, 40)> easy
self.rect_medium <rect(960, 440, 200, 40)> medium
self.rect_hard <rect(960, 390, 200, 40)> hard      


Butones
Este es x 960 y 540
Estos son rect  easy, medium y hard
<rect(960, 590, 200, 40)>
<rect(960, 640, 200, 40)>
<rect(960, 690, 200, 40)>
-----------
(960, 590) 
(960, 640)
(960, 690)



def _prep_msg(self, msg):
		""" Turn msg into a rendered image and center text on the button """
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.x, self.y  = self.rect.center

		self.msg_image_rect.center = self.x - 300, self.y# Esto provoca que el texto este desalineado con respecto
														 # al cuadro tengo que alinear a ambos
														 # Aqui estoy alineando el texto con respecto al cuadro

			'''