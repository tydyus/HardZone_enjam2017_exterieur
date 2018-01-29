import pygame
from pygame.locals import *
import time

from assets import *
from terrain import *
from player import *
from pnj import *

class carte():	
    carte = "assets/carte/lvl0.txt"
    victoire = [0,0]
    lvl = 3
    def __init__(self):
        carte.re()

    def reload(self):
        carte.re()
    def re():
        if player.lvl == 0:
            print("   -> lvl.0")
            carte.carte = "assets/carte/lvl0.txt"
            pnj.list = []
            pnj.create("tourelle",9,2)
            pnj.create("tourelle",9,8)
            player.x = 1
            player.lx = player.x *50
            player.y = 5
            player.ly = player.y *50
            carte.victoire = [20,5]
            player.victoire = carte.victoire
        if player.lvl == 1:
            print("   -> lvl.1")
            carte.carte = "assets/carte/lvl1.txt"
            pnj.list = []
            pnj.create("tourelle",10,3)
            pnj.create("tourelle",10,7)
            pnj.create("tourelle",11,5)
            pnj.create("pnj",4,3,"right",3)
            pnj.create("pnj",4,7,"right",3)
            player.x = 1
            player.lx = player.x *50
            player.y = 5
            player.ly = player.y *50
            carte.victoire = [20,5]
            player.victoire = carte.victoire
        if player.lvl == 2:
            print("   -> lvl.2")
            carte.carte = "assets/carte/lvl2.txt"
            pnj.list = []
            pnj.create("pnj",8,7,"back",6)
            pnj.create("pnj",16,3,"left",5)
            pnj.create("pnj",11,6,"right",5)
            player.x = 1
            player.lx = player.x *50
            player.y = 5
            player.ly = player.y *50
            carte.victoire = [20,5]
            player.victoire = carte.victoire
        if player.lvl == 3:
            print("   -> lvl.3")
            carte.carte = "assets/carte/lvl3.txt"
            pnj.list = []
            pnj.create("pnj",3,1,"front",8)
            pnj.create("pnj",5,1,"front",4)
            pnj.create("pnj",5,9,"back",3)
            pnj.create("pnj",7,9,"back",8)
            pnj.create("pnj",8,9,"back",8)
            pnj.create("tourelle",10,3)
            pnj.create("pnj",18,9,"left",4)
            pnj.create("pnj",16,4,"right",4)
            pnj.create("tourelle",17,1)
            player.x = 1
            player.lx = player.x *50
            player.y = 5
            player.ly = player.y *50
            carte.victoire = [20,5]
            player.victoire = carte.victoire