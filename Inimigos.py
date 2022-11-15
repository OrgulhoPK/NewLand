import pygame as pg
from Configs import Config

class Inimigos: 
    def __init__(self,posXY,posWH):
        self.X = posXY[0]
        self.Y = posXY[1]
        self.posWH = posWH
        self.movimento = 4
        self.animation_count = 0
        self.mov_direita = False
        self.mov_esquerda = False
        self.mov_cima = False
        self.mov_baixo = False 
        self.hitbox = (self.X-2 ,self.Y-2,35,35)


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
        
