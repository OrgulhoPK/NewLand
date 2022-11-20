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
        self.vida = 10
        self.dano = 10
        self.visible= True
        self.hitbox = pg.Rect(self.X-2 ,self.Y-2,35,35)
        
    
    def movimento(self,x,y):
        if (self.Y<=433 and self.Y>=288) and (x<= 433 and x>= 127):
            self.angle = math.atan2(self.X-y,self.Y-x)
            x_vel = math.cos(self.angle)* (random.randint(1,5))
            y_vel = math.sin(self.angle)* (random.randint(1,5))
            self.X -= int(x_vel)
            self.Y -= int(y_vel)
        else:
            self.X = random.randint(288,433)
            self.Y = random.randint(127,433)


    def hit(self):
        if self.vida>0:
            self.vida -=1
            
        else:
            self.visible = False


    def desenhar(self,tela):
        if self.visible:
            mob_y = random.randint(288,433)
            mob_x = random.randint(127,433)
            self.movimento(mob_x,mob_y)

            if self.animation_count +1 >= 28:
                self.animation_count = 0
            self.animation_count += 1

            x,y,l,a = self.X,self.Y,self.posWH[0],self.posWH[1]
            pg.draw.rect(tela,Config.COR_Tela,self.hitbox,2)
            pg.draw.rect(tela,Config.COR_InimigoTest,pg.rect.Rect(x,y,l,a))

            self.hitbox = pg.Rect(self.X-2 ,self.Y-2,35,35)
            pg.draw.rect(tela,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,40,8))
            pg.draw.rect(tela,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,40 - (4 * (10-self.vida)),8))



        
