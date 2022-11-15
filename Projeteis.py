import math
import pygame as pg
import random 

from Configs import Config
from Imagens import Imagem



class Projetil:
    def __init__(self,x,y,raio,mousex,mousey):
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
        self.raio = raio

    def desenha(self,tela):

        self.contador += 1

        if self.contador +1 >=8:
            self.atk = False            
            self.x -= int(self.x_vel)
            self.y -= int(self.y_vel)
            
            pg.draw.circle(tela,(0,0,0),(self.x,self.y), self.raio)

        if self.atk and self.contador <=7:
            tela.blit(pg.transform.scale(Imagem.atk[self.contador], (64,64)),(self.x-32,self.y-45))
        

    def colisaoProjetil(self,alvo) -> bool:
        return ((self.y - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + self.raio>alvo.hitbox[1]) and 
            (self.x + self.raio>alvo.hitbox[0] and 
            self.x - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))