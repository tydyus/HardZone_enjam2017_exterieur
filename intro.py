import pygame
from pygame.locals import *
import time

from assets import *
from terrain import *
from player import *
from pnj import *
from carte import *

class intro():
    time = 0
    end = 670
    def intro():
        intro.time += 1
        # arrivé dans le monde
        s1 = 35
        #vue du hl
        s2 = 30
        #hl donne popo
        s3 = 30
        #bois popo
        s4 = 25
        #warning
        s5 = 40
        #hard zone
        s6 = 30
        #
        end = s1+s2+s3+s4+s5+s6
        if intro.time < s1:
            assets.img["scene1"].render()
        elif intro.time < s1+s2:
            assets.img["scene2"].render()
        elif intro.time < s1+s2+s3:
            assets.img["scene3"].render()
        elif intro.time < s1+s2+s3+s4:
            assets.img["scene4"].render()
        elif intro.time < s1+s2+s3+s4+s5:
            assets.img["scene5"].render()
        elif intro.time < s1+s2+s3+s4+s5+s6:
            assets.img["scene6"].render()
