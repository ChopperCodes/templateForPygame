import pygame
from clsBackground import Background

class Game(object):
	
	def __init__(self, config):
		self.isDone = False
		self.size = config['size']
		self.fps = config['fps']
		self.bgImage = config['bgImage']
		self.caption = config['caption']

		pygame.init()
		pygame.display.set_caption(self.caption)

		self.screen= pygame.display.set_mode(self.size)
		self.background= Background( screen=self.screen, bgImage=self.bgImage )
		self.clock = pygame.time.Clock()

	def __closeGame(self):
		return True

	def logic(self, spot):
		response = spot
		self.background.show()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.isDone = self.__closeGame()
		
			response = self.interpretSpot(response, event)
		
		pygame.display.update()
		pygame.display.flip()	
		self.clock.tick(self.fps)
		return response

	def interpretSpot(self, spot, event):
		keys = pygame.key.get_pressed()
		if spot == 'init':
			spot = 'title'
		elif spot == 'title' and keys[pygame.K_SPACE]:
			self.isDone = self.__closeGame()

		return spot

	def quit(self):
		pygame.quit()
