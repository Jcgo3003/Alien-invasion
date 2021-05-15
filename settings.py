
class Settings: 
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (66, 95, 192)

		#Ship Settings
		self.ship_speed = 15
		
		# Bullet settings
		self.bullet_speed = 20.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (255, 255, 255)
		self.bullets_allowed = 3