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
        self.speed = 8
        self.angle = math.atan2(y-mousey,x-mousex)
        self.x_vel = math.cos(self.angle)* self.speed
        self.y_vel = math.sin(self.angle)* self.speed
        self.atk = False
        self.contador = 0
        self.raio = raio
        self.multiplicador = 3
        self.anim = 0


    def desenha(self,tela):

        self.contador += 1


        if self.contador +1 >=9:
            self.atk = False            
            self.x -= int(self.x_vel)
            self.y -= int(self.y_vel)
            
            pg.draw.circle(tela,(0,0,0),(self.x,self.y), self.raio)
            self.anim += 1


            if self.anim + 1 >= 21:
                self.anim = 0
            
            
            
            tela.blit(pg.transform.scale(Imagem.S_fireball1[self.anim//2],(32,32)),(self.x-16,self.y-16))
        
        


    def ataque(self,lista):
        for i in lista:
            colide = self.colisaoProjetil(i)
            if colide:
                i.hit('dano')
                



    def colisaoProjetil(self,alvo) -> bool:
        return ((self.y - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + self.raio>alvo.hitbox[1]) and 
            (self.x + self.raio>alvo.hitbox[0] and 
            self.x - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))
