import pygame as pg

from Configs import Config
from Imagens import Imagem
from Projeteis import Projetil

class Jogador:
    def __init__(self,posXY, posWH): #(self, x, y, widht, height)
        self.X = posXY[0]
        self.Y = posXY[1]
        self.posWH = posWH #tamanhoOBJ
        self.movimento = 4
        self.animation_count = 0    #é só um contador de animação (só pra trocar o frame)
        self.mov_direita = False
        self.mov_esquerda = False
        self.mov_cima = False
        self.mov_baixo = False
        self.atk = False
        self.countatk = 0
        self.hitbox = (self.X + 17,self.Y+8,31,57)
        

    #criar funções para movimentar o jogador

    def esquerda(self):
        self.X -= self.movimento


    def direita(self):

        self.X += self.movimento

    def cima(self):

        self.Y -= self.movimento

    def baixo(self):

        self.Y  += self.movimento

    def atualizar_posicao(self):
        pass



    def desenhar(self,tela):
        #tratamento da animação (desenho)
        if self.animation_count +1 >= 28:
            self.animation_count = 0

        self.animation_count +=1


        if pg.mouse.get_pressed()[0]:
            self.atk = True
            
        if self.atk:
            self.countatk +=1
            if self.countatk +1 >= 8:
                self.countatk = 0
                self.atk = False


        if not self.atk:
            if not self.mov_esquerda and not self.mov_direita and not self.mov_cima and not self.mov_baixo:

                tela.blit(pg.transform.scale(Imagem.andarP1B[0], (64,64)),(self.X,self.Y))
            
            elif self.mov_direita or (self.mov_direita and (self.mov_cima or self.mov_baixo)):
                
                tela.blit(pg.transform.scale(Imagem.andarP1D[self.animation_count//4], (64,64)),(self.X,self.Y))

                self.mov_direita = False

            elif self.mov_esquerda or (self.mov_esquerda and (self.mov_cima or self.mov_baixo)):
                tela.blit(pg.transform.scale(pg.transform.flip(Imagem.andarP1D[self.animation_count//4],True,False), (64,64)),(self.X,self.Y))
                self.mov_esquerda = False

            elif self.mov_cima:
                tela.blit(pg.transform.scale(Imagem.andarP1C[self.animation_count//4], (64,64)),(self.X,self.Y))
                
                self.mov_cima = False

            elif self.mov_baixo:
               
                tela.blit(pg.transform.scale(Imagem.andarP1B[self.animation_count//4], (64,64)),(self.X,self.Y))
                self.mov_baixo = False
        self.hitbox = (self.X + 17,self.Y+8,31,57)
        pg.draw.rect(tela,Config.COR_Tela,self.hitbox,2)
