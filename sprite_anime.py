import pygame
from pygame.locals import *
from PIL import Image

from spriteM import *

class anime:

    def __init__(self, imgObj_spriteM, tick, frameListe, x=0, y=0):
        self.time = 0
        self.tick = tick
        self.img = imgObj_spriteM
        self.frame = frameListe
        self.etat = 0
        self.etatFinal = 0
        self.x = x
        self.y = y

    def render(self, x="none", y="none", repeat="repeat", rot=0):
        if x == "none":
            x = self.x
        if y == "none":
            y = self.y
        if self.frame[1] == "to":
            a = self.frame[0]
            b = self.frame[2]
            liste = []
            frame = 0
            for i in range(b):
                if i < a:
                    pass
                else:
                    liste.append(i)
                frame +=1
            self.frame = liste
                
        self.time += 1
        
        if rot ==0:
            self.img.render(x, y, (self.etat))
        else:
            self.img.render_rot(rot, x, y, (self.etat))
            
        if self.time >= self.tick:
            self.time = 0
            if self.etat == (len(self.frame)-1):
                if repeat == "repeat":
                    self.etat = 0
                if repeat == "no-repeat":
                    self.etatFinal = 1

            if self.etatFinal == 0:
                self.etat += 1
            else:
                return "end-anime"
            

            


