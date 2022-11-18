import pygame as pg
import math
from Configs import Config
import random

class Inimigos: 
    def __init__(self,posXY,posWH):
        self.X = posXY[0]
        self.Y = posXY[1]
        self.posWH = posWH
        self.speed = 4
        self.animation_count = 0
        self.mov = False

        self.hitbox = (self.X-2 ,self.Y-2,35,35)
    
    #def movimento(self,x,y):
    #    if not self.mov:
    #        self.angle = math.atan2(self.X-y,self.Y-x)
    #        x_vel = math.cos(self.angle)* self.speed
     #       y_vel = math.sin(self.angle)* self.speed
     #       self.X -= int(x_vel)
     #       self.Y -= int(y_vel)


    def desenhar(self,tela):

        if self.animation_count +1 >= 28:
            self.animation_count = 0

        self.animation_count += 1

        x,y,l,a = self.X,self.Y,self.posWH[0],self.posWH[1]
        
        self.hitbox = (self.X-2 ,self.Y-2,35,35)
        pg.draw.rect(tela,Config.COR_Tela,self.hitbox,2)
        pg.draw.rect(tela,Config.COR_InimigoTest,pg.rect.Rect(x,y,l,a))

    def dano(self):
        print ('hit')
        
