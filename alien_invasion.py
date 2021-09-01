import sys
import pygame
from settings import Settings
from ship import Ship
from character import Character
from bullet import Bullet
from alien import Alien
from star import Star
from raindrop import Raindrop
import random


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

		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.character = Character(self)
		

		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()


		self.rain = pygame.sprite.Group()

		self._create_fleet()
		self._create_rain()

	def _create_sky_stars(self, alien_possitions, alien_width, alien_height):
		""" Create a grid of stars and avoiding the aliens images """
		# Create a grid of stars
		star = Star(self)
		star_width, star_height = star.rect.size

		# Getting the space available
		available_space_x = self.settings.screen_width

		# Getting rid of 1/4 of the beginning of the screen
		available_space_y = self.settings.screen_height 
		
		# Getting all the space diponible for the stars 
		number_stars_x = self.settings.screen_width // (star_width * 3)

		# Giving some space between the ground and the sky, one fifth from the ground will make it
		number_rows_stars = (available_space_y // star_height) // 3


		# Create a sky full of stars
		x_list = []
		y_list = []

		for x, y in alien_possitions:
			if x not in x_list:
				x_list.append(x)
			if y not in y_list:
				y_list.append(y)

		y = 0 

		for row_number_star in range(number_rows_stars):
			
			# Reseting x
			x = 0


			for star_number in range(number_stars_x):
			# Create a star, only if its not on the alien way
				star = Star(self)
				star.rect.x = star_width + (star_width * 3) * star_number
				star.rect.y = star.rect.height + 2 * star.rect.height * row_number_star

				r = random.randint(0, 10)


				# Creating stars when there is not any alien, so a row of stars without interruption
				if (star.rect.y < y_list[y] and not(r % 2)):
					self.stars.add(star)


				elif(star.rect.y > y_list[y] and star.rect.y < (y_list[y] + alien_height and not(r % 2))):
					if (star.rect.x < x_list[x]):
						self.stars.add(star)
						

					elif(star.rect.x > x_list[x] + alien_width and not(r % 2)):
						self.stars.add(star)
						x += 1 
						if (x >= len(x_list)):
							x = len(x_list) - 1
							# self.stars.add(star)

				# Creating a row of stars when there an alien ship on the way
				elif (star.rect.y > (y_list[y] + alien_height) and not(r % 2)):
					# Getting the next alien possition for y
					y += 1
					self.stars.add(star)
					if y >= len(y_list):
						y = len(y_list) - 1
					
	

	def _create_fleet(self):
		""" Create the fleet of aliens. """
		# Create an alien and find the number of alienst in a row.
		# Spacing betwwen each alien is equal to one alien width.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine the number or rows of alien that fit on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)


		# Variable to save the alien possitions
		alien_possitions = []

		# Create the full fleet of aliens.
		for row_number in range(number_rows):

			for alien_number in range(number_aliens_x):
				# Create an alien and place it in the row, and saving then
				alien_possitions.append(self._create_alien(alien_number, row_number))
				

		self._create_sky_stars(alien_possitions, alien_width, alien_height)

	def _create_alien(self, alien_number, row_number):
		""" Create an alien and place it in the row. """
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

		# Sending the aliens possitions
		return [alien.rect.x, alien.rect.y]

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _create_rain(self):
		""" Get some rain into the game """
		raindrop = Raindrop(self)
		raindrop_width, raindrop_height = raindrop.rect.size

		available_space_x = self.settings.screen_width
		number_raindrops = available_space_x // (3 * raindrop_width)

		r = random.randint(0,100)

		if not (r % 90):

			for x in range(number_raindrops):
				r = random.randint(0, 100)
					
				if not(r % 7):	
					self._create_raindrops(x)


	def _create_raindrops(self, x):
		"""Create raindrops"""
		raindrop = Raindrop(self)
		raindrop_width, raindrop_height = raindrop.rect.size
		raindrop.x = raindrop_width + 3 * raindrop_width * x
		raindrop.rect.x = raindrop.x
		raindrop.rect.y = raindrop.y 
		# raindrop.rect.y = raindrop_height + 3 * raindrop_height * row_number

		self.rain.add(raindrop)

	def _update_rain(self):
		""" Let's star the rain falling"""
		self.rain.update()
		self._create_rain()
		# The horizon a few meters above the ground
		horizon = 100
		for raindrops in self.rain.copy():
			if raindrops.rect.bottom == (self.settings.screen_height - horizon):
				self.rain.remove(raindrops)


	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			self._update_screen()

			#Adding movement updates
			self.ship.update()
			self._update_bullets()


			self._update_aliens()
			self._update_rain()



	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)


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

	def _update_bullets(self):
		""" Update position of bullets and get rid of old bullets. """
		# Update bullet positions.
		self.bullets.update()


		# Get rid of the bullets that have disappeared. 
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions():
		""" Respond to bullet-alien collisions."""
		# Remove any bullets and aliens that have collide
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		# Check for empty groups and creating a new fleet
		if not self.aliens:
			# Destroy exitsting bullets and create new fleet.
			self.bullets.empty()
			self._create_fleet()


	def _update_aliens(self):
		"""Check if the fleet is at an edge,
		then update the possitions of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		
		self.aliens.update()


	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
			

		self.aliens.draw(self.screen)
		self.stars.draw(self.screen)
		self.character.blitme()

		self.rain.draw(self.screen)

		pygame.display.flip()



if __name__ == "__main__":
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()



""" He logrado varios avances con respecto de las estrellas,
    Tengo que lograr que los espacios vacios donde no estan las 
    nave alienigenas esten a reventar de estrellas y eventualmente
    utilizar randint para hacer que paresca que aparecen y desaparesen
    """ 