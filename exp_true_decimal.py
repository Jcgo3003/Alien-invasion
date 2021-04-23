boleano = True
numeroDecimal = 10.5
comprobacion = 15

if boleano and numeroDecimal < comprobacion:
	print("Un boleano y un decimal se pueden utilizar juntos")

""" 
En el desarrollo del juego alien_ivation, el autor utilizo un boleano y un decimal para 
hacer una sentencia, no sabia que es posible hacerlo

En concreto el codigo se encuentra en el archivo ship.py
Aqui un extracto

def update(self):
		Update the ship's position based on the movement flag.
		if self.moving_right and self.rect.right < self.screen_rect.right:
		# if self.moving_right:
			# self.rect.x += 1
			self.x += self.settings.ship_speed
"""