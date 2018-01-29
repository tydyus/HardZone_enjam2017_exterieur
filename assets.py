import pygame
from pygame.locals import *
import time

from spriteM import *
from sprite_anime import *
from font import *
from sound import *

class assets:

	#resize
	facteur = 1
	#couleur
	color_font = (193,196,192)
	color_screen = (137,176,192)
	color_white = (255,255,255)
	color_grey = (127,127,127)
	color_dark = (0,0,0)
	color_yellow = (251,230,36)
	color_blue = (12,131,197)
	color_purple = (182,26,171)
	color_red = (209,90,80)
	color_red2 = (223,107,97)
	color_green = (89,179,109)
	color_orange =(172,97,45)
	color_orange2 =(172,83,45)
	color_orange3 =(172,50,45)
	color_equip = [color_white, color_blue, color_dark, color_purple, color_grey, color_yellow]
	#font
	font_texte = "font/larabiefont_rg.ttf"

    #dico d'image
	img = {
		"scene1": spriteM("assets/img/intro/scene1.png"),
		"scene2": spriteM("assets/img/intro/scene2.png"),
		"scene3": spriteM("assets/img/intro/scene3.png"),
		"scene4": spriteM("assets/img/intro/scene4.png"),
		"scene5": spriteM("assets/img/intro/scene5.png"),
		"scene6": spriteM("assets/img/intro/scene6.png"),
		"fond": spriteM("assets/img/fond.png"),
		"menu": spriteM("assets/img/menu.png"),
		"game over": spriteM("assets/img/fond_mort.png"),
		"next lvl": spriteM("assets/img/fond_lvl.png"),
		"victory": spriteM("assets/img/fond_victoire.png"),
		"piques": spriteM("assets/img/piques.png"),
		"sol1": spriteM("assets/img/sol1.png"),
		"sol2": spriteM("assets/img/sol2.png"),
		"sol3": spriteM("assets/img/sol3.png"),
		"sol4": spriteM("assets/img/sol4.png"),
		"sol5": spriteM("assets/img/sol5.png"),
		"sol6": spriteM("assets/img/sol6.png"),
		"sol7": spriteM("assets/img/sol7.png"),
		"sol8": spriteM("assets/img/sol8.png"),
		"sol9": spriteM("assets/img/sol9.png"),
		"sol10": spriteM("assets/img/sol10.png"),
		"sortie": spriteM("assets/img/sortie.png"),
		"trou": spriteM("assets/img/trou.png"),
		"trouHD": spriteM("assets/img/trouHD.png"),
		"trouHG": spriteM("assets/img/trouHG.png"),
		"trouBD": spriteM("assets/img/trouBD.png"),
		"trouBG": spriteM("assets/img/trouBG.png"),
		"trouH": spriteM("assets/img/trouH.png"),
		"trouB": spriteM("assets/img/trouB.png"),
		"trouD": spriteM("assets/img/trouD.png"),
		"trouG": spriteM("assets/img/trouG.png"),
		"trouHB": spriteM("assets/img/trouHB.png"),
		"trouGD": spriteM("assets/img/trouGD.png"),
		"trouAD": spriteM("assets/img/trouAD.png"),
		"trouAG": spriteM("assets/img/trouAG.png"),
		"mur1": spriteM("assets/img/mur1.png"),
		"mur2": spriteM("assets/img/mur2.png"),
		"case": spriteM("assets/img/case.png"),
		"grille": spriteM("assets/img/grille.png"),
		"!": spriteM("assets/img/exclamation.png"),
		"?": spriteM("assets/img/interogation.png"),
		"tourelle": spriteM("assets/img/tourelle.png"),
		"player_ombre": spriteM("assets/img/player_ombre.png"),
		"player_front": spriteM("assets/img/player_front.png"),
		"player_back": spriteM("assets/img/player_back.png"),
		"player_left": spriteM("assets/img/player_left.png"),
		"player_right": spriteM("assets/img/player_right.png"),
		"pnj_front": spriteM("assets/img/pnj_front.png"),
		"pnj_back": spriteM("assets/img/pnj_back.png"),
		"pnj_left": spriteM("assets/img/pnj_left.png"),
		"pnj_right": spriteM("assets/img/pnj_right.png")
	}
	img["pnj_front"].frames(50,100)
	img["pnj_back"].frames(50,100)
	img["pnj_left"].frames(50,100)
	img["pnj_right"].frames(50,100)
	img["player_front"].frames(50,100)
	img["player_back"].frames(50,100)
	img["player_left"].frames(50,100)
	img["player_right"].frames(50,100)

	#dico son
	sound = {
		"pause": sound("assets/sound/switch.wav"),
		"!": sound("assets/sound/excla.wav"),
		"?": sound("assets/sound/intero.wav"),
		"dash": sound("assets/sound/dash.wav"),
		"fond": sound("assets/sound/Wasteland Overdrive Looped.wav", "fond")
	}

	font = {
		"death": font("death: ",color_orange,(686,622,"")),
		"lvl": font("lvl: ",color_orange,(1050,622,""))
	}
	
	def resize(newsize):
		assets.facteur = newsize[0]/spriteM.screen_x
		spriteM.facteur = assets.facteur
		for cle in assets.img:
			assets.img[cle].resize(assets.facteur)
	
		return 1
	def volume(valeur):
		if sound.volume == valeur:
			sound.volume = 0
		else:
			sound.volume = valeur
		sound.set_volume()
