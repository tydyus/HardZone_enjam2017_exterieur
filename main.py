import pygame
from pygame.locals import *
import time

from assets import *
from game import *
from menu import *
from spriteM import *


pygame.init()

pygame.display.update()
#time.sleep(3)
continuer = 1
game_etat = "menu"
print("launching")
#spriteM.screen_size(1100,650)
while continuer:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		elif event.type==VIDEORESIZE:
			print("resize")
			
	if game_etat == "menu":
		game_etat = menu.menu()
	if game_etat == "partie":
		game_etat = game.partie()
	if game_etat == "exit":
    		continuer = 0
		
	pygame.event.pump()
	pygame.display.update()