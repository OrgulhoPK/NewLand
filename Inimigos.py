import pygame as pg
import math
from Configs import *
import random
from Jogador import Jogador

class Inimigo: 
    def __init__(self,posXY,posWH,personagem:Personagem):
        self.x = posXY[0]
        self.y = posXY[1]
        self.posWH = posWH
        self.inimigovx = 0
        self.inimigovy = 0
        self.speed = 0.8
        self.atk = False

        self.anim_mov = 0
        self.mov = False
        self.vida = personagem.vida
        self.dano = personagem.dano
        self.visible= True
        self.hitbox = pg.Rect(self.x+17,self.y+34,31,31)
        self.raio = 500
        self.personagem = personagem
         
    def movimento(self,jogador1:Jogador,jogador2:Jogador):
        distancia1 = math.sqrt(((self.hitbox.centerx - jogador1.hitbox.centerx)**2) +
                                ((self.hitbox.centery- jogador1.hitbox.centery)**2))

        distancia2 = math.sqrt(((self.hitbox.centerx - jogador2.hitbox.centerx)**2) +
                                ((self.hitbox.centery- jogador2.hitbox.centery)**2))

        if distancia1 < distancia2:
            alvo_x= jogador1.X +32
            alvo_y= jogador1.Y + 32
            dist = math.sqrt((alvo_x - self.x) ** 2 +
            (alvo_y - self.y) ** 2)
            
            if dist > 1:

                self.inimigovx = alvo_x - self.x
                self.inimigovy = alvo_y - self.y
                
                norma = math.sqrt(self.inimigovx ** 2 + self.inimigovy ** 2)
                self.inimigovx /= norma
                self.inimigovy /= norma
            
                self.inimigovx *= self.speed
                self.inimigovy *= self.speed
            else:
                self.inimigovx = 0
                self.inimigovy = 0

            self.x += self.inimigovx
            self.y += self.inimigovy
        else:
            alvo_x= jogador2.X +32
            alvo_y= jogador2.Y + 32
            dist = math.sqrt((alvo_x - self.x) ** 2 +
            (alvo_y - self.y) ** 2)
            
            if dist > 1:

                self.inimigovx = alvo_x - self.x
                self.inimigovy = alvo_y - self.y
                
                norma = math.sqrt(self.inimigovx ** 2 + self.inimigovy ** 2)
                self.inimigovx /= norma
                self.inimigovy /= norma
            
                self.inimigovx *= self.speed
                self.inimigovy *= self.speed
            else:
                self.inimigovx = 0
                self.inimigovy = 0

            self.x += self.inimigovx
            self.y += self.inimigovy


        
        


    def hit(self):
        if self.vida>0:
            self.vida -=1
            
        else:
            self.visible = False

    def areaameaca(self,alvo) -> bool:
        return ((self.y +16- self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y +16 + self.raio>alvo.hitbox[1]) and 
            (self.x +16+ self.raio>alvo.hitbox[0] and 
            self.x +16- self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))



    def desenhar(self,tela):
        esq_Dir = self.personagem.sprites[0]
        cima = self.personagem.sprites[1]
        baixo = self.personagem.sprites[2]
        ataque = self.personagem.sprites[3]
        if self.visible:
            if self.anim_mov +1 >= 28:
                self.anim_mov = 0
            self.anim_mov += 1
            #desenha o mob
            if not self.atk:
                if self.inimigovx == 0 and self.inimigovy == 0:
                    tela.blit(pg.transform.scale(baixo[0], (64,64)),(self.x,self.y))
                
                elif self.inimigovx>0 or (self.inimigovx>0 and (self.inimigovy>0 or self.inimigovy<0)):                    
                    tela.blit(pg.transform.scale(esq_Dir[self.anim_mov//4], (64,64)),(self.x,self.y))
                    self.mov_direita = False

                elif self.inimigovx<0 or (self.inimigovx<0 and (self.inimigovy>0 or self.inimigovy<0)):
                    tela.blit(pg.transform.scale(pg.transform.flip(esq_Dir[self.anim_mov//4],True,False), (64,64)),(self.x,self.y))
                    self.mov_esquerda = False

                elif self.inimigovy<0:
                    tela.blit(pg.transform.scale(cima[self.anim_mov//4], (64,64)),(self.x,self.y))  
                    self.mov_cima = False

                elif self.inimigovy>0:
                    tela.blit(pg.transform.scale(baixo[self.anim_mov//4], (64,64)),(self.x,self.y))
                    self.mov_baixo = False
            #pg.draw.circle(tela,(COR_Tela),(x+16,y+16), self.raio)



            pg.draw.rect(tela,COR_Tela,self.hitbox,2)
            #atualiza o hitbox do mob e barra de vida
            self.hitbox = pg.Rect(self.x+17,self.y+34,31,31)
            pg.draw.rect(tela,(255,0,0),(self.x+17,self.y,40,8))
            pg.draw.rect(tela,(0,128,0),(self.x+17,self.y,40 - (4 * (10-self.vida)),8))



        
