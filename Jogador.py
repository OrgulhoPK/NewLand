from typing import Tuple
import pygame as pg

from Configs import Config
from Imagens import Imagem


class Jogador:
    def __init__(self,posXY, posWH): #(self, x, y, widht, height)
        self.posXY = posXY # atualização da posicao
        self.posWH = posWH #tamanhoOBJ
        self.movimento = 4
        self.scroll = [0,0]
        self.animation_count = 0
        self.mov_direita = False
        self.mov_esquerda = False
        

    #criar funções para movimentar o jogador

    def esquerda(self):
        self.scroll[0] += self.movimento


    def direita(self):
        self.scroll[0] -= self.movimento

    def cima(self):
        self.scroll[1] += self.movimento

    def baixo(self):
        self.scroll[1] -= self.movimento


    def atualizar_posicao(self):
        pass



    def desenhar(self,tela):
        #tratamento da animação (desenho)
        if self.animation_count +1 >= 28:
            self.animation_count = 0
        
        # posição x e y, largura e altura
        x,y,l,a = self.posXY[0],self.posXY[1],self.posWH[0],self.posWH[1]

        
        if self.mov_esquerda and self.mov_direita:
            tela.blit(pg.transform.scale(Imagem.andar[self.animation_count//28], (64,64)),(x-self.scroll[0],y-self.scroll[1]))
            self.animation_count = 0
            self.mov_esquerda = False
            self.mov_direita = False    

        elif not self.mov_esquerda and not self.mov_direita:
            self.animation_count = 0
            tela.blit(pg.transform.scale(Imagem.andar[self.animation_count//28], (64,64)),(x-self.scroll[0],y-self.scroll[1]))
        
        while(self.mov_direita):
        #elif self.mov_direita:
            tela.blit(pg.transform.scale(Imagem.andar[self.animation_count//4], (64,64)),(x-self.scroll[0],y-self.scroll[1]))         
            self.animation_count +=1

        while(self.mov_esquerda):
        #elif self.mov_esquerda:
            tela.blit(pg.transform.scale(pg.transform.flip(Imagem.andar[self.animation_count//4],True,False), (64,64)),(x-self.scroll[0],y-self.scroll[1]))
            
            self.animation_count +=1
            
        



        #pg.drawn.rect(tamanho da tela, cor do objeto, posicao_x,y , proporção do player)
        #pg.draw.rect(
        #    tela,
        #    Config.COR_PlayerTest,pg.rect.Rect(x-self.scroll[0],y-self.scroll[1],l,a))