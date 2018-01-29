import pygame
from pygame.locals import *
import time

from assets import *
from terrain import *
from player import *
from pnj import *
from carte import *
from intro import *

class game:	
	def partie():
		print("-> game")		
		
		clock = pygame.time.Clock()
		FPS = 60
		continuer = 1
		pause = 0
		assets.sound["fond"].run() # asset son base

		#carte	
		player.map_tab = terrain.gen(carte.carte)
		lvl = carte()
		end = ""
		grille = 0
		terrain.grille = grille
		player.grille = grille

		#boucle
		while continuer:

			#fps
			clock.tick(FPS)

			#event
			click = "free"
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
					return "exit"
				elif event.type==VIDEORESIZE:
					pass
					refresh = assets.resize(event.size)
				elif event.type == KEYDOWN:
					click = "busy"
					#pause
					while pause:
						if event.key == K_ESCAPE:
							assets.sound["pause"].run()
							pause = 0
							click = "free"
							print("<<pause")
					if event.key == K_ESCAPE and click == "busy":
						pass #pause: perma activate/desactivate
						assets.sound["pause"].run()
						pause = 1
						print(">>pause")
					#grille
					if event.key == K_g and click == "busy":
						intro.time = 1000
						if grille == 1:
							grille = 0
						else:
							grille = 1
						terrain.grille = grille
						player.grille = grille
					if event.key == K_l and click == "busy":
						player.end = "next lvl"
						end = "next lvl"
					#son
					if event.key == K_s and click == "busy":
						assets.volume(0.3)
					end = player.end
					if event.key == K_SPACE:
						if end == "game over":
							lvl.reload()	
							player.map_tab = terrain.gen(carte.carte)
							player.death += 1
							player.end = ""
							end = ""
						elif end == "next lvl":
							player.lvl += 1
							if player.lvl > carte.lvl:
								end = "victory"
								player.end = end
								pass
							lvl.reload()
							player.map_tab = terrain.gen(carte.carte)
							player.end = ""
							end = ""
						if end == "victory": 
							pass
					##
					if event.key == K_UP:
    						player.mouv("back")
					if event.key == K_DOWN:
    						player.mouv("front")
					if event.key == K_RIGHT:
    						player.mouv("right")
					if event.key == K_LEFT:
    						player.mouv("left")
					if event.key == K_LSHIFT or event.key == K_RSHIFT:
    						player.dash()
				if event.type == KEYUP:
    					if event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
    							player.stop_mouv()
					
				
			assets.img["fond"].render()
			assets.font["death"].render("death: %d" % player.death)
			assets.font["lvl"].render("lvl: %d" % player.lvl)
			terrain.carte(carte.carte)

			end = player.end
			if end == "game over":
				assets.img["game over"].render()
			elif end == "next lvl":
				if player.lvl > carte.lvl:
					end = "victory"
					player.end = end
				else:
					assets.img["next lvl"].render()
			if end == "victory": 
				assets.img["victory"].render()
			if intro.time < intro.end:
				intro.intro()
			pygame.event.pump()
			pygame.display.update()