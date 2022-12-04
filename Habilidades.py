from Configs import *
from Imagens import *
import math,random
import pygame as pg



#Nessa classe, estão sendo tratadas de maneira individual 
# os ataques basicos e habilidades

class melee:
    def __init__(self,raio,sprites):
        self.raio = raio
        self.x = None
        self.y = None
        self.contador = 0
        self.spriteBasica= sprites

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
            tela.blit(pg.transform.scale(self.spriteBasica[self.contador],(128,128)),(alvo.x-32,alvo.y-32))
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
            tela.blit(pg.transform.scale(self.spriteBasica[self.contador],(128,128)),(alvo.x-32,alvo.y-32))
            alvo.hit()
            self.contador+=1
        
    def BasicaRange(self,x,y,velxy):
        velx = velxy[0]
        vely = velxy[1]
        x = x+32
        y = y+40
        if velx == 0 and vely == 0:
            return (Projetil(x,y,self.raio,x+1,y,self.spriteBasica))      
        else:
            return (Projetil(x,y,self.raio,x+velx, y+vely,self.spriteBasica))

            #self.projeteis.append(Projetil(self.jogador1.X+32,self.jogador1.Y+45,5,mouse_x,mouse_y))      


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
    def __init__(self,x,y,raio,mousex,mousey,sprite):
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
        self.sprite = sprite

    def desenha(self,tela):


        self.atk = False            
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

          
        pg.draw.circle(tela,(0,0,0),(self.x,self.y),self.raio)
        tela.blit(pg.transform.scale(self.sprite[self.anim//2],(64,64)),(self.x-16,self.y-16))
        if self.anim + 1 >= 16:
            self.anim = 0   
        self.anim += 1
        


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
