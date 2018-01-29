import pygame
from pygame.locals import *
from PIL import Image

from sprite_anime import *
from assets import *

class spriteM:

    
    counter = 0 #nombre d'image dans le sprite manager
    screen_x = 1100
    screen_y = 650
    fenetre = pygame.display.set_mode((screen_x,screen_y)) #l'on défini la fenetre de pygame dans le l'objet spriteM
    facteur = 1
    def __init__(self, path, x=0, y=0):
        
        spriteM.counter += 1
        self.name = "SpriteM_n." + str(spriteM.counter)
        self.nameSRC = "SpriteM_SRC_n." + str(spriteM.counter) 
        self.x = x
        self.y = y
        self.img = {(self.name):pygame.image.load(path).convert_alpha(), (self.nameSRC):pygame.image.load(path).convert_alpha()}
        self.path = path
        self.multiFrame = 0
        

    def screen_size(x,y):
        spriteM.screen_x = x
        spriteM.screen_y = y
        spriteM.fenetre = pygame.display.set_mode((x,y),HWSURFACE|DOUBLEBUF|RESIZABLE)

    def load(self, path, x="none", y="none"):    # met l'image en base de donnee à la place de celle d'origine

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y

        self.path = path
        self.img = {(self.name ):pygame.image.load(path).convert_alpha(), (self.nameSRC):pygame.image.load(path).convert_alpha()}

    def resize(self, facteur):
        screen=pygame.display.set_mode((int(spriteM.screen_x*facteur),int(spriteM.screen_y*facteur)),HWSURFACE|DOUBLEBUF|RESIZABLE)
        rect = self.img[self.nameSRC].get_rect()
        #print(self.name," ",rect)
        picture = self.img[self.nameSRC]
        picture = pygame.transform.scale(picture, (int(picture.get_rect()[2]*facteur),int(picture.get_rect()[3]*facteur)))
        self.img[self.name] = picture

    def frames(self, tx, ty, maxFrames=0, path="none"): #tx/ty: taille d'une frames, maxFrames: nbr de frames du sprite
        if path != "none":
            load(path)
            
        nbrFramesX = int((self.img[(self.name )].get_size()[0] // tx)-1)
        nbrFramesY = int((self.img[(self.name )].get_size()[1] // ty)-1)

        self.multiFrame = 1
        nbrframe = 0
        #print("creat ",self.name)
        for ii in range(nbrFramesY+1):
            for i in range(nbrFramesX+1):
                self.img[nbrframe] = ((tx*i), (ty*ii), tx, ty)
                #print((nbrframe),": ",(tx*i)," ", (ty*ii)," ", tx," ", ty)
                nbrframe += 1
                if maxFrames != 0 and maxFrames == nbrframe:
                    break
                           

    def render(self, x="none", y="none", frame=0):
        if x == "none":
            x = self.x
        if y == "none":
            y = self.y

        if self.multiFrame == 0:
            spriteM.fenetre.blit(self.img[(self.name )], (x*spriteM.facteur,y*spriteM.facteur))
        else:
            img = self.img[(self.name)]
            spriteM.fenetre.blit(img.subsurface(self.img[frame]), (x*spriteM.facteur,y*spriteM.facteur))
        #print("img rendu en x:",self.x," y:",self.y)

    def render_rot(self, angle=0, x="none", y="none", frame=0):

        if x == "none":
            x = self.x
        if y == "none":
            y = self.y
            
        if self.multiFrame == 0:
            image = self.img[(self.name)]
        else:
            img = self.img[(self.name)]
            image = img.subsurface(self.img[frame])
            
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        
        spriteM.fenetre.blit(rot_image, (x*spriteM.facteur,y*spriteM.facteur))

        #print("img rendu en x:",x," y:",y, ". Avec un angle de ",angle," dg.")
        


        
        

    
