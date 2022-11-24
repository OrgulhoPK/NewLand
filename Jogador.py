import pygame as pg
from Configs import *

from Personagens import Personagem
class Jogador:
    def __init__(self,posXY, posWH,personagem:Personagem): #(self, x, y, widht, height)
        self.X = posXY[0]
        self.Y = posXY[1]
        self.posWH = posWH #tamanhoOBJ
        self.movimento = 4
        #referente ao personagem
        self.vida = 10
        self.dano = 10
        #referente ao personagem vivo ou nao
        self.visible= True
        self.personagem = personagem

        #referente à animação do personagem    
        self.anim_mov = 0    #é só um contador de animação (trocar o frame)
        self.mov_direita = False
        self.mov_esquerda = False
        self.mov_cima = False
        self.mov_baixo = False
        self.atk = False
        self.countatk = 0



        #hitbox = X, Y , Largura, Altura  Rect()
        self.hitbox = pg.Rect(self.X+17,self.Y+8,31,57)

    #criar funções para movimentar o jogador
    def esquerda(self):
        self.X -= self.movimento
    def direita(self):
        self.X += self.movimento
    def cima(self):
        self.Y -= self.movimento
    def baixo(self):
        self.Y  += self.movimento

    #Função que calcula colisão com uma lista de objetos
    def colisao(self,alvo):
        collision_tolerance = 8
        for i in alvo:
            colide = self.hitbox.colliderect(i)
            if colide:          
                if abs(i.top - self.hitbox.bottom) < collision_tolerance:
                    self.hitbox.bottom -= collision_tolerance
                    self.cima()
                if abs(i.bottom - self.hitbox.top) < collision_tolerance:
                    self.hitbox.bottom += collision_tolerance
                    self.baixo()
                if abs(i.right - self.hitbox.left) < collision_tolerance:
                    self.hitbox.left += collision_tolerance
                    self.direita()  
                if abs(i.left - self.hitbox.right) < collision_tolerance:
                    self.hitbox.right -= collision_tolerance
                    self.esquerda()
                    

                        

    def disparo(self):
        pass

    def hit(self):
        if self.vida>0:
            self.dano = True
            self.vida -=1
        else:
            self.visible = False




    def desenhar(self,tela):
        esq_Dir = self.personagem.sprites[0]
        cima = self.personagem.sprites[1]
        baixo = self.personagem.sprites[2]
        ataque = self.personagem.sprites[3]

        #Contador de animação (desenho)
        if self.visible:
            if self.anim_mov+1 >= 28:
                self.anim_mov = 0
            self.anim_mov +=1

            #Tratamento da animação de ataque
            if pg.mouse.get_pressed()[0]:
                self.atk = True
            if self.atk:   
                if self.countatk +1 >= 9:
                    self.countatk = 0
                    self.atk = False

                if self.countatk <=8:
                    tela.blit(pg.transform.scale(ataque[self.countatk], (64,64)),(self.X,self.Y))
        
                self.countatk +=1
            

            if not self.atk:
                if not self.mov_esquerda and not self.mov_direita and not self.mov_cima and not self.mov_baixo:
                    tela.blit(pg.transform.scale(baixo[0], (64,64)),(self.X,self.Y))
                
                elif self.mov_direita or (self.mov_direita and (self.mov_cima or self.mov_baixo)):
                    
                    tela.blit(pg.transform.scale(esq_Dir[self.anim_mov//4], (64,64)),(self.X,self.Y))
                    self.mov_direita = False

                elif self.mov_esquerda or (self.mov_esquerda and (self.mov_cima or self.mov_baixo)):
                    tela.blit(pg.transform.scale(pg.transform.flip(esq_Dir[self.anim_mov//4],True,False), (64,64)),(self.X,self.Y))
                    self.mov_esquerda = False

                elif self.mov_cima:
                    tela.blit(pg.transform.scale(cima[self.anim_mov//4], (64,64)),(self.X,self.Y))  
                    self.mov_cima = False

                elif self.mov_baixo:
                    tela.blit(pg.transform.scale(baixo[self.anim_mov//4], (64,64)),(self.X,self.Y))
                    self.mov_baixo = False

            #atualizar posicao do hitbox
            self.hitbox = pg.Rect(self.X+17,self.Y+8,31,57)
            pg.draw.rect(tela,COR_Tela,self.hitbox,2)
            pg.draw.rect(tela,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,40,8))
            pg.draw.rect(tela,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,40 - (4 * (10-self.vida)),8))
