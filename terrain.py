import pygame
from pygame.locals import *
from random import randint
from random import seed
import time

from assets import *
from player import *
from pnj import *
from carte import *


class terrain ():
    
    map_tab = []
    grille = 1
    def gen(carte):
        terrain.map_tab = []
        with open(carte, "r") as ligne:
            x=0
            y=0
            for i in ligne:
                x=0
                tab =[]
                for ii in i:
                    tab.append(ii)
                    x+=1
                terrain.map_tab.append(tab)
                y+=1
        return terrain.map_tab
    def look_map(carte,xS,yS,look):
        
                
        with open(carte, "r") as ligne:
            x = 0
            y = 0
            for i in ligne:
                x=0
                for ii in i:
                    if x == xS and y == yS:
                        if ii == look:
                            return 1
                        else:
                            return 0
                    x += 1
                y += 1
            return 0
    
    def carte(carte):
        ii = ""
        graine = 0
        for y in range(len(terrain.map_tab)):
            for x in range(len(terrain.map_tab[0])-1):
                ii = terrain.map_tab[y][x]
                #mur
                if ii == "#": 
                    graine +=5
                    seed(graine)
                    assets.img[("mur%d" % randint(1, 2))].render(x*50,y*50)
                #trou
                elif ii == "0":
                    h = terrain.look_map(carte,x,y-1,"0")
                    b = terrain.look_map(carte,x,y+1,"0")
                    g = terrain.look_map(carte,x-1,y,"0")
                    d = terrain.look_map(carte,x+1,y,"0")
                    if (h,b,g,d) == (1,1,1,1):
                        assets.img["trou"].render(x*50,y*50)
                    elif (h,b,g,d) == (0,1,1,1):
                        assets.img["trouH"].render(x*50,y*50)
                    elif (h,b,g,d) == (1,0,1,1):
                        assets.img["trouB"].render(x*50,y*50)
                    elif (h,b,g,d) == (1,1,0,1):
                        assets.img["trouG"].render(x*50,y*50)
                    elif (h,b,g,d) == (1,1,1,0):
                        assets.img["trouD"].render(x*50,y*50)
                    elif (h,b,g,d) == (0,1,0,1):
                        assets.img["trouHG"].render(x*50,y*50)
                    elif (h,b,g,d) == (0,1,1,0):
                        assets.img["trouHD"].render(x*50,y*50)
                    elif (h,b,g,d) == (1,0,0,1):
                        assets.img["trouBG"].render(x*50,y*50)
                    elif (h,b,g,d) == (1,0,1,0):
                        assets.img["trouBD"].render(x*50,y*50)
                    elif (h,b,g,d) == (0,0,0,1):
                        assets.img["trouAG"].render(x*50,y*50)
                    elif (h,b,g,d) == (0,0,1,0):
                        assets.img["trouAD"].render(x*50,y*50)
                    elif (h,b,g,d) == (0,0,1,1):
                        assets.img["trouHB"].render(x*50,y*50)
                    elif (h,b,g,d) == (1,1,0,0):
                        assets.img["trouGD"].render(x*50,y*50)
                    else: 
                        assets.img["trouH"].render(x*50,y*50)
                #sol
                else:
                    graine +=5
                    seed(graine)
                    assets.img[("sol%d" % randint(1, 10))].render(x*50,y*50)
                if terrain.grille == 1:
                    assets.img["grille"].render(x*50,y*50)
                if [x,y] == player.victoire:
                    assets.img["sortie"].render(x*50,y*50)
                #player
                if x == player.x:
                    player.render()
                #pnj
                pnj.render(x,y)
        