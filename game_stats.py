from pathlib import Path


class GameStats:
	""" Tracking statistics for alien_invasion """

	def __init__(self, ai_game):
		""" Iniciate statistics """
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an active state.
		self.game_active = True

		# Start game in an inactive state
		self.game_active = False

		# High score that should never be reset
		self.high_score = 0

		# Reading the savedata
		self.read_savedata()


	def reset_stats(self):
		""" Initialize statistics that can change during the game """
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def read_savedata(self):
		""" Creating or reading a save data file """
		filename = Path("savedata.txt")
		filename.touch(exist_ok=True)

		file = open(filename, "r+")
		score_savedata = file.read()
		if score_savedata:
			self.high_score = int(score_savedata)
		else: 
			self.high_score = 0


	def savedata(self):
		""" Updating the high score if necesary """
		filename = ("savedata.txt")

		file = open(filename, "r+")
		score_savedata = file.read()

		if score_savedata:
			if self.high_score > int(score_savedata):
				file = open(filename, "w+") 
				file.write(str(self.high_score))
		else:
			file.write(str(self.high_score))

		file.close()
		


		
