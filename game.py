from config.config import *
from lib.clsGame import Game

game = Game(config)

spot='init'
while not game.isDone:
	spot = game.logic(spot)

game.quit()
