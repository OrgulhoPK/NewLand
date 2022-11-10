import pygame as pg
from Configs import Config

class Inimigos: 
    def __init__(self,posXY,posWH):
        self.posXY = posXY
        self.posWH = posWH
        self.movimento = 4
        self.animation_count = 0
        self.mov_direita = False
        self.mov_esquerda = False
        self.mov_cima = False
        self.mov_baixo = False 
        


    def desenhar(self,tela):
        if self.animation_count +1 >= 28:
            self.animation_count = 0

        self.animation_count += 1

        x,y,l,a = self.posXY[0],self.posXY[1],self.posWH[0],self.posWH[1]
        

        pg.draw.rect(tela,Config.COR_InimigoTest,pg.rect.Rect(x,y,l,a))
        
