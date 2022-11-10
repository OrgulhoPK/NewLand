from typing import Tuple
import pygame as pg

from Configs import Config
from Imagens import Imagem


class Jogador:
    def __init__(self,posXY, posWH): #(self, x, y, widht, height)
        self.posXY = posXY # atualização da posicao
        self.posWH = posWH #tamanhoOBJ
        self.movimento = 4
        self.scroll = [0,0] # é o que move o personagem ao clicar uma tecla
        self.animation_count = 0    #é só um contador de animação (só pra trocar o frame)
        self.mov_direita = False
        self.mov_esquerda = False
        self.mov_cima = False
        self.mov_baixo = False
        

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

        self.animation_count +=1
        
        # posição x e y, largura e altura
        x,y,l,a = self.posXY[0],self.posXY[1],self.posWH[0],self.posWH[1]

            

        if not self.mov_esquerda and not self.mov_direita and not self.mov_cima and not self.mov_baixo:
            tela.blit(pg.transform.scale(Imagem.andarP1B[0], (64,64)),(x-self.scroll[0],y-self.scroll[1]))
        
        
        elif self.mov_direita or (self.mov_direita and (self.mov_cima or self.mov_baixo)):
            tela.blit(pg.transform.scale(Imagem.andarP1D[self.animation_count//4], (64,64)),(x-self.scroll[0],y-self.scroll[1]))         
            self.mov_direita = False
        elif self.mov_esquerda or (self.mov_esquerda and (self.mov_cima or self.mov_baixo)):
            tela.blit(pg.transform.scale(pg.transform.flip(Imagem.andarP1D[self.animation_count//4],True,False), (64,64)),(x-self.scroll[0],y-self.scroll[1]))
            self.mov_esquerda = False
        elif self.mov_cima:
            tela.blit(pg.transform.scale(Imagem.andarP1C[self.animation_count//4], (64,64)),(x-self.scroll[0],y-self.scroll[1]))
            self.mov_cima = False
        elif self.mov_baixo:
            tela.blit(pg.transform.scale(Imagem.andarP1B[self.animation_count//4], (64,64)),(x-self.scroll[0],y-self.scroll[1]))
            self.mov_baixo = False


            
        



        #pg.drawn.rect(tamanho da tela, cor do objeto, posicao_x,y , proporção do player)
        #pg.draw.rect(
        #    tela,
        #    Config.COR_PlayerTest,pg.rect.Rect(x-self.scroll[0],y-self.scroll[1],l,a))