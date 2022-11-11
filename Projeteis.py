import math
import pygame as pg
from Configs import Config
from Imagens import Imagem



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
        self.atk = False
        self.contador = 0

    def desenha(self,tela):  
        if self.contador +1 >=8:
            contador = 0
            self.atk = False
            self.x -= int(self.x_vel)
            self.y -= int(self.y_vel)
            pg.draw.circle(tela,(0,0,0),(self.x,self.y), 5)
        self.contador += 1
        if self.atk and self.contador <=7:
            tela.blit(pg.transform.scale(Imagem.atk[self.contador], (64,64)),(self.x-32,self.y-45))

        