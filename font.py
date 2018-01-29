import pygame
from pygame.locals import *
import time

from spriteM import *
from sprite_anime import *

class font:
    pygame.font.init()

    facteur = 1

    def __init__ (self, texte, couleur, placement, taille_font=15, police_font = "none"):
        self.texte=texte
        self.couleur=couleur
        self.placement=placement #(x,y,point de rendu[haut gauche de base, "rd" possible])
        self.xDecal = 0
        self.yDecal = 0
        if police_font == "none":
            self.myfont = pygame.font.SysFont('Arial', taille_font)
            self.myfontSRC = pygame.font.SysFont('Arial', taille_font)
        else:
            self.myfont = pygame.font.Font(police_font, taille_font)
            self.myfontSRC = pygame.font.Font(police_font, taille_font)
        self.phrase = self.myfont.render(texte, True, couleur)
        self.police_font = police_font
        self.taille_font = taille_font

    def resize (self, facteur):
        font.facteur = facteur
        if self.police_font == "none":
            self.myfont = pygame.font.SysFont('Arial', int(self.taille_font*facteur))
        else:
            self.myfont = pygame.font.Font(self.police_font, int(self.taille_font*facteur))


    def render (self, texte="none", placement = "none"):
        
        if placement == "none":
            placement = self.placement
        if texte != "none":
            self.phrase = self.myfont.render(texte, True, self.couleur)
            self.texte = texte
        else:
            self.phrase = self.myfont.render(self.texte, True, self.couleur)
        if self.placement[2] == "bas-droit":
            self.xDecal = pygame.Surface.get_rect(self.phrase)[2]
            self.yDecal = pygame.Surface.get_rect(self.phrase)[3]
        elif self.placement[2] == "bas-gauche":
            self.yDecal = pygame.Surface.get_rect(self.phrase)[3]
        elif self.placement[2] == "haut-droit":
            self.xDecal = pygame.Surface.get_rect(self.phrase)[2]
        elif self.placement[2] == "centre":
            self.xDecal = pygame.Surface.get_rect(self.phrase)[2]/2
            self.yDecal = pygame.Surface.get_rect(self.phrase)[3]/2
        spriteM.fenetre.blit(self.phrase,(int((placement[0]*font.facteur)-self.xDecal),int((placement[1]*font.facteur)-self.yDecal)))