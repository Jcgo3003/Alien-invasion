
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
		self.ship_limit = 3
		
		# Bullet settings
		self.bullet_speed = 30.0
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (255, 255, 255)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed = 3.0
		self.fleet_drop_speed = 150
		
		# Fleet_ditection of 1 reprensents right; -1 represents left.
		self.fleet_direction = 1

		# Rain settings
		self.rain_speed = 1.0
		self.rain_direction = 1

		# How quickly the game speeods up
		self.speedup_scale = 1.1

		# How quickly the alien point values increase 
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		""" Initialize settinns that change throught the game. """
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# Fleet_direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1

		# Scoring 
		self.alien_points = 50

	def level_easy(self):
		""" Initialize settings for a easy game """
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# Fleet_direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1

	def level_medium(self):
		""" Initialize settings for a easy game """
		self.ship_speed = 3.0
		self.bullet_speed = 5.0
		self.alien_speed = 2.0

		# Fleet_direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1

	def level_hard(self):
		""" Initialize settings for a easy game """
		self.ship_speed = 4.5
		self.bullet_speed = 7.0
		self.alien_speed = 3.0

		# Fleet_direction of 1 represents right; -1 represents left. 
		self.fleet_direction = 1

	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)


	









		