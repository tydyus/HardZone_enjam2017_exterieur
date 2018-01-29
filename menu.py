import pygame
from pygame.locals import *
import time

from assets import *

class menu:
	def menu():
		print("-> menu")
		refresh = 1
		continuer = 1
		
		while continuer:
			
			click = "free"
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
					return "exit"
				elif event.type == VIDEORESIZE:
					refresh = assets.resize(event.size)
				elif event.type == MOUSEBUTTONDOWN and click == "free":
					click = "busy"	
					return "partie"				
			
			assets.img["menu"].render()
			#maj assets
			pygame.event.pump()
			pygame.display.update()
					