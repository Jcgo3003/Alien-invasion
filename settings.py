
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

		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# Fleet_ditection of 1 reprensents right; -1 represents left.
		self.fleet_direction = 1

		# Rain settings
		self.rain_speed = 0.0
		self.rain_direction = 1

		