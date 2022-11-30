from Configs import *
from Imagens import *
import math,random
import pygame as pg



#Nessa classe, estão sendo tratadas de maneira individual 
# os ataques basicos e habilidades

class melee:
    def __init__(self,raio):
        self.raio = raio
        self.x = None
        self.y = None
        self.contador = 0

    def sleep(self):
        pass

    #mob e a duelista
    def Basica(self,x,y,dados,velxy):
        
        self.x = x
        self.y = y
        tela = dados[0]
        alvo = dados[1]
        velx,vely= velxy
        rect = pg.Rect((self.x+(32*velx)),self.y+20, 80, 40)
        
        if rect.colliderect(alvo.hitbox):
            if self.contador+1 >=5:
                self.contador = 0
            tela.blit(pg.transform.scale(Imagem.hitDamage[self.contador],(128,128)),(alvo.x-32,alvo.y-32))
            alvo.hit()
            self.contador+=1

    def EspecialD(self,x,y,dados,velxy):
        self.x = x
        self.y = y
        tela = dados[0]
        alvo = dados[1]
        velx,vely= velxy
        rect = pg.Rect((self.x+(32*velx)),self.y+20, 80, 40)
        
        if rect.colliderect(alvo.hitbox):
            if self.contador+1 >=5:
                self.contador = 0
            tela.blit(pg.transform.scale(Imagem.hitDamage[self.contador],(128,128)),(alvo.x-32,alvo.y-32))
            alvo.hit()
            self.contador+=1
        
    


            # - - - - - - - - -
            # 1 1 + 0 0 0 0 + -
            # 1 1 0 0 0 0 0 0 -
            # 1 1 + 0 0 0 0 + -
            # - - - - - - - - -


    def BasicaGuaraci():
        pass

        # - - - - - - - - -
        # 1 1 0 + - - - - -
        # 1 1 0 + - - - - -
        # 1 1 0 + - - - - -
        # - - - - - - - - -

  
    def ataque(self,lista):
        pass

    def colisao(self,alvo) -> bool:
        return ((self.y - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + self.raio>alvo.hitbox[1]) and 
            (self.x + self.raio>alvo.hitbox[0] and 
            self.x - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))





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


        if self.contador +1 >=17:
            self.atk = False            
            self.x -= int(self.x_vel)
            self.y -= int(self.y_vel)
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
