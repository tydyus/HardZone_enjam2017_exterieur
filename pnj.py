import pygame
from pygame.locals import * 
from math import sqrt

from assets import *
from player import *

class pnj ():
    list = []
    time = 0

    def create(type = "tourelle",x = 0,y = 0,sens_deplacement="right",distance=0):
        pnj.list.append(pnj(type,x,y,sens_deplacement,distance))

    def __init__(self,type,x,y,sens_deplacement,distance):
        if type == "tourelle":
            self.yeux = 100
            self.vu = 0
            self.oreilles = 150
            self.entendu = 0
            self.anime = "none"
        elif type == "pnj":
            self.yeux = 80
            self.vu = 0
            self.oreilles = 130
            self.entendu = 0
            if distance > 0:
                self.anime = 1
            else:
                self.anime = 0
            self.sens = "front"
            self.frame = 0
            self.sens_deplacement = sens_deplacement
            self.distance = distance
            self.distance_parcourue = 0
            self.vitesse = 0.25
        self.animeY = 0
        self.animeX = 0
        self.type = type
        self.x = x
        self.y = y
    def __exit__(self, *err):
        self.close() 
    def ligneDeVue(self,xM,yM,xPJ,yPJ):
        xPJ = xPJ+25
        xM = xM+25
        yPJ = yPJ+40
        yM = yM+40
        facteurX = (xPJ - xM)/20 
        facteurY = (yPJ - yM)/20
        x2 = -1
        y2 = -1
        #print((xPJ - xM),facteurX,(yPJ - yM),facteurY,yPJ)
        #print("start")
        for i in range(20):
            x = int((xPJ-(facteurX*i))/50)
            y = int((yPJ+(facteurY*i))/50)
            if x == x2 and y == y2:
                pass
            else:
                #print(x,y,player.map_tab[y][x])
                if player.map_tab[y][x] == "#":
                    if player.grille == 1:
                        pygame.draw.line(spriteM.fenetre, assets.color_green, (xM,yM+40), (xPJ,yPJ+40))
                    return 0
            x2 = x
            y2 = y
        if player.grille == 1:
            pygame.draw.line(spriteM.fenetre, assets.color_red, (xM,yM+40), (xPJ,yPJ+40))
        return 1
    def render(x,y):
        for monstre in pnj.list:
            if player.grille == 1:
                pygame.draw.circle(spriteM.fenetre, assets.color_red, (int(monstre.x*50+25+monstre.animeX),int(monstre.y*50+80+monstre.animeY)), monstre.yeux,2)
                pygame.draw.circle(spriteM.fenetre, assets.color_green, (int(monstre.x*50+25+monstre.animeX),int(monstre.y*50+80+monstre.animeY)), monstre.oreilles,2)

            if monstre.x == x:
                
                if monstre.anime == "none":
                    assets.img[monstre.type].render(monstre.x*50,monstre.y*50)
                else:
                    if monstre.anime == 0 or player.end != "":
                        assets.img[(monstre.type+"_"+monstre.sens)].render(monstre.x*50,monstre.y*50)
                    elif monstre.anime == 1:
                        if pnj.time > player.ratio_frame:
                            monstre.frame += 1
                        if monstre.frame > 2:
                            monstre.frame = 0
                        monstre.distance_parcourue += monstre.vitesse
                        if monstre.sens_deplacement == "right":
                            monstre.animeX +=monstre.vitesse
                            if monstre.distance_parcourue > (monstre.distance*50):
                                monstre.sens_deplacement = "left"
                                monstre.distance_parcourue = 0
                        if monstre.sens_deplacement == "left":
                            monstre.animeX -=monstre.vitesse
                            if monstre.distance_parcourue > (monstre.distance*50):
                                monstre.sens_deplacement = "right"
                                monstre.distance_parcourue = 0
                        if monstre.sens_deplacement == "front":
                            monstre.animeY +=monstre.vitesse
                            if monstre.distance_parcourue > (monstre.distance*50):
                                monstre.sens_deplacement = "back"
                                monstre.distance_parcourue = 0
                        if monstre.sens_deplacement == "back":
                            monstre.animeY -=monstre.vitesse
                            if monstre.distance_parcourue > (monstre.distance*50):
                                monstre.sens_deplacement = "front"
                                monstre.distance_parcourue = 0
                        assets.img[(monstre.type+"_"+monstre.sens_deplacement)].render(int(monstre.x*50+monstre.animeX),int(monstre.y*50+monstre.animeY), monstre.frame)

                    
                a = player.lx - int(monstre.x*50+monstre.animeX)
                b = player.ly - int(monstre.y*50+monstre.animeY)
                c = sqrt(a*a+b*b)
                
                if c < 100 and monstre.ligneDeVue(int(monstre.x*50+monstre.animeX),int(monstre.y*50+monstre.animeY),player.lx,player.ly):
                    assets.img["!"].render(int(monstre.x*50+monstre.animeX),int(monstre.y*50+monstre.animeY))
                    if monstre.vu == 0:
                        assets.sound["!"].run()
                        monstre.vu = 1
                if c < (monstre.yeux-3) and monstre.ligneDeVue(int(monstre.x*50+monstre.animeX),int(monstre.y*50+monstre.animeY),player.lx,player.ly):
                    player.end = "game over"
                elif c < monstre.oreilles and monstre.ligneDeVue(int(monstre.x*50+monstre.animeX),int(monstre.y*50+monstre.animeY),player.lx,player.ly):
                    assets.img["?"].render(int(monstre.x*50+monstre.animeX),int(monstre.y*50+monstre.animeY))
                    if monstre.entendu == 0:
                        assets.sound["?"].run()
                        monstre.entendu = 1
                else:
                    monstre.vu = 0
                    monstre.entendu = 0
        if pnj.time > player.ratio_frame:
            pnj.time = 0
        else:
            pnj.time += 1
                
        