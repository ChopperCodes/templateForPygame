import pygame

class Background:

	def __init__(self, screen, bgImage, pos=0):
		self.screen = screen
		self.bgImage = bgImage
		self.pos = pos
		self.__loadImages()

	def __loadImages(self):
		self.bg = []
		for img in self.bgImage:
			self.bg.append( pygame.image.load(img).convert() )

	def show(self):
		self.screen.blit(self.bg[self.pos], [0,0])
