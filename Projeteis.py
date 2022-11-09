import math
import pygame as pg
from Configs import Config



class Projetil:
    def __init__(self,x,y,mousex,mousey):
        self.x = x
        self.y = y
        self.mousex = mousex
        self.mousey = mousey
        self.speed = 15
        self.angle = math.atan2(y-mousey,x-mousex)
        self.x_vel = math.cos(self.angle)* self.speed
        self.y_vel = math.sin(self.angle)* self.speed
        

    def desenha(self,display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pg.draw.circle(display,(0,0,0),(self.x,self.y), 5)