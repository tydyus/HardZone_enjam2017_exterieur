import pygame
from pygame.locals import *
import time

from assets import *

class player ():
    x = 2
    y = 2
    lx = 100
    ly = 100
    sens = "front"
    anime = 0
    time = 0
    frame = 0
    ratio_frame = 25
    map_tab =[]
    dash_charge = 1000
    grille = 0
    death = 0
    lvl = 0
    end = ""
    victoire = [0,0]
        
    def render():
        #timer/autre
        if player.dash_charge < 1000 and player.end == "":
            player.dash_charge += 1
        if player.dash_charge > 500:
            color = assets.color_orange
        elif player.dash_charge > 300:
            color = assets.color_orange2
        else:
            color = assets.color_orange3
        pygame.draw.rect(spriteM.fenetre, color,(425,621,int(player.dash_charge/4),20))
        #victoire
        if [player.x,player.y+1] == player.victoire:
            player.end = "next lvl"
        #rendu/mouvement
        x = player.lx 
        y = player.ly
        player.time += 1
        assets.img["player_ombre"].render(x,y)
        if player.anime == 0:
            if player.grille == 1:
                assets.img["case"].render(x,y)
            assets.img[("player_"+player.sens)].render(x,y)
        else:
            if player.grille == 1:
                assets.img["case"].render(x,y)
            assets.img[("player_"+player.sens)].render(x,y, player.frame)
            #move
            xc = (player.lx+25)
            yc = (player.ly+90)
            if player.sens == "front" and player.map_tab[int((yc+10)/50)-1][int(xc/50)] == "." and player.end == "":
                player.ly += 1
            if player.sens == "back" and player.map_tab[int((yc-10)/50)-1][int(xc/50)] == "." and player.end == "":
                player.ly -= 1
            if player.sens == "left" and player.map_tab[int(yc/50)-1][int((xc-10)/50)] == "." and player.end == "":
                player.lx -= 1
            if player.sens == "right" and player.map_tab[int(yc/50)-1][int((xc+10)/50)] == "." and player.end == "":
                player.lx += 1
            player.x = int(player.lx/50)
            player.y = int(player.ly/50)
        

            
            
            
            if player.time > player.ratio_frame:
                player.frame += 1
                if player.frame == 3:
                    player.frame = 0
                player.time = 0
    def mouv(sens):
        player.anime = 1
        player.sens = sens
    
    def dash():
        
        xc = (player.lx+25)
        yc = (player.ly+90)
        dash_valeur = player.dash_charge/10
        if player.sens == "front" and player.map_tab[int((yc+10+dash_valeur)/50)-1][int(xc/50)] == "." and dash_valeur > 30:
            player.ly += dash_valeur
            player.dash_charge = 0
            assets.sound["dash"].run()
        if player.sens == "back" and player.map_tab[int((yc-10-dash_valeur)/50)-1][int(xc/50)] == "." and dash_valeur > 30:
            player.ly -= dash_valeur
            player.dash_charge = 0
            assets.sound["dash"].run()
        if player.sens == "left" and player.map_tab[int(yc/50)-1][int((xc-10-dash_valeur)/50)] == "." and dash_valeur > 30:
            player.lx -= dash_valeur
            player.dash_charge = 0
            assets.sound["dash"].run()
        if player.sens == "right" and player.map_tab[int(yc/50)-1][int((xc+10+dash_valeur)/50)] == "." and dash_valeur > 30:
            player.lx += dash_valeur
            player.dash_charge = 0
            assets.sound["dash"].run()

    def stop_mouv():
        player.anime = 0

        