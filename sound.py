import pygame
from pygame.locals import *
import time

class sound:

    pygame.init()
    volume = 0.3 #0.3
    pygame.mixer.music.set_volume(volume)

    def __init__(self, path, type = "event"):
        self.type = type
        if type == "event":
            self.son = pygame.mixer.Sound(path)
        elif type == "fond":
            pygame.mixer.music.load(path)
        
    def run(self):
        if self.type == "event":
            self.son.play() 
        elif self.type == "fond":
            pygame.mixer.music.play(-1)

    def stop(self):
        if self.type == "event":
            self.son.stop()
        elif self.type == "fond":
            pygame.mixer.music.stop()

    def set_volume():
        pygame.mixer.music.set_volume(sound.volume)