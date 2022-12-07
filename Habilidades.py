from Configs import *
from Imagens import *
import math,random
import pygame as pg



#Nessa classe, estão sendo tratadas de maneira individual 
# os ataques basicos e habilidades

class Skill:
    def __init__(self,raio,sprites,x=None,y=None):
        self.raio = raio
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.speed = 1
        self.contador = 0
        self.time_efeito = 0
        self.pos = 0 #serve somente para contar uma nova posição para o x e y
        self.sprite= sprites


    def sleep(self):
        pass

    #mob e a duelista
    def Basica(self,x,y,dados,velxy):
        
        self.x = x
        self.y = y
        tela = dados[0]
        alvos = dados[1]
        velx,vely= velxy
        if velx == 0:
            velx = 1
        rect = pg.Rect((self.x+(32*velx)),self.y+20, 80, 40)
        
        for alvo in alvos:
            if rect.colliderect(alvo.hitbox):
                if self.contador+1 >=5:
                    self.contador = 0
                tela.blit(pg.transform.scale(self.sprite[self.contador],(128,128)),(alvo.x-32,alvo.y-32))
                alvo.hit()
                self.contador+=1

    def EspecialD(self,x,y,dados,velxy):#Especial duelista
        self.x = x
        self.y = y
        tela = dados[0]
        alvos = dados[1]
        velx,vely= velxy
        if velx ==0:
            velx =1
        rect = pg.Rect((self.x+(32*velx)),self.y+20, 80, 40)
        for alvo in alvos:
            if rect.colliderect(alvo.hitbox):
                if self.contador+1 >=5:
                    self.contador = 0
                tela.blit(pg.transform.scale(self.sprite[self.contador],(128,128)),(alvo.x-32,alvo.y-32))
                alvo.hit()
                self.contador+=1
        
    def BasicaRange(self,nome,x,y,velxy): #AtaqueRange
        velx = velxy[0]
        vely = velxy[1]
        x = x+32
        y = y+40
        if nome == 'Soldado':
            if velx < 0 and vely == 0:
                return (Projetil(nome,x,y,self.raio,x-1,y,self.sprite))      
            else:
                return (Projetil(nome,x,y,self.raio,x+velx, y+vely,self.sprite))
        else:
            if velx == 0 and vely == 0:
                return (Projetil(nome,x,y,self.raio,x+1,y,self.sprite))      
            else:
                return (Projetil(nome,x,y,self.raio,x+velx, y+vely,self.sprite))

    def EspecialH(self,x,y,dados): #Especial Clerigo
        self.x = x
        self.y = y
        tela = dados[0]
        alvos = dados[1]
        
        for alvo in alvos:
            if self.colisao(alvo,self.raio):
                tela.blit(pg.transform.scale(self.sprite[self.contador],(64,79)),(alvo.x,alvo.y-10))
                alvo.hit()
                alvo.stun = True
                if self.contador+1 >=5:
                    self.contador = 0
                self.contador+=1

    def BasicaGuaraci(self,x,y,dados,velxy,mov):
        self.x = x
        self.y = y
        tela = dados[0]
        alvos = dados[1]
        velx,vely= velxy
        rect = None
        if velx == -1:
            rect = pg.Rect(self.x+5,self.y+20, 20, 35)
        elif velx == 0:
            velx = 1 
            rect = pg.Rect(self.x+32,self.y+20, 20, 35)
        elif velx == 1:
            rect = pg.Rect((self.x+(32*velx)),self.y+20, 20, 35)
        for alvo in alvos:
            if rect.colliderect(alvo.hitbox):
                tela.blit(pg.transform.scale(self.sprite[2],(128,128)),(alvo.x-32,alvo.y-32))
                alvo.x += mov*1.5*velx
                alvo.hit()
                alvo.stun = True

    def EspecialG(self,dados,jogador):
        tela = dados[0]
        if jogador.vida < jogador.hpmax:
            jogador.vida += 3

        tela.blit(pg.transform.scale(self.sprite,(72,64)),(jogador.x-5,jogador.y+25))


    def EspecialJ(self,mousexy,dados): #Especial Shaman
        self.x = mousexy[0]
        self.y = mousexy[1]
        tela = dados[0]
        alvos = dados[1]

        for alvo in alvos:
            if self.colisao(alvo,self.raio):
                if self.contador+1 >=36:
                    self.contador = 0
                tela.blit(pg.transform.scale(self.sprite[self.contador//4],(72,64)),(alvo.x-5,alvo.y+25))
                alvo.hit()

                self.contador+=1

    def Teleporte(self,tela,aliados,inimigos):
        listTarget = aliados + inimigos
        self.time_efeito+= 1
        if self.time_efeito>50:
            if self.time_efeito==51:
                self.x = random.randint(400,1000)
                self.y = random.randint(250,600)
            
            tela.blit(pg.transform.scale(self.sprite[self.contador//4],(64,40)),(self.x,self.y+20))
            pg.draw.circle(tela,(0,0,0),(self.x+32,self.y+40),self.raio,2)
            pg.draw.circle(tela,(55,28,15),(self.x+32,self.y+40),self.raio*10.4,2)
            for i in listTarget:
                if self.colisao(i,(self.raio*10)):
                    alvo_x= i.x
                    alvo_y= i.y+10
                    dist = math.sqrt((alvo_x - self.x) ** 2 +
                    (alvo_y - self.y) ** 2)
                    
                    if dist > 1:
                        self.vx = alvo_x - self.x
                        self.vy = alvo_y - self.y
                        
                        norma = math.sqrt(self.vx ** 2 + self.vy ** 2)
                        self.vx /= norma
                        self.vy /= norma
                    
                        self.vx *= self.speed
                        self.vy *= self.speed
                    else:
                        self.vx = 0
                        self.vy = 0
                    self.x += self.vx
                    self.y += self.vy
                
                if self.vx == 0 and self.vy ==0:
                    print('colidiu')

            self.contador +=1
            
            if self.contador +1 >=16:
                self.contador = 0
                

                

    def colisao(self,alvo, raio) -> bool:
        return ((self.y - raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + raio>alvo.hitbox[1]) and 
            (self.x + raio>alvo.hitbox[0] and 
            self.x - raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))
 


class Projetil:
    def __init__(self,nome,x,y,raio,mousex,mousey,sprite):
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
        self.nome = nome

    def desenha(self,tela):

        self.atk = False            
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        if self.nome == 'Heitor': 
            tela.blit(pg.transform.scale(self.sprite[self.anim//2],(64,64)),(self.x,self.y-32))
        
        if self.nome == 'Jurupari':       
            tela.blit(pg.transform.scale(Imagem.S_fireball1[self.anim//2],(32,32)),(self.x-16,self.y-16))
        
        if self.nome == 'Soldado':
            tela.blit(pg.transform.scale(self.sprite[self.anim//4],(64,32)),(self.x-32,self.y-32))
        
        
        if self.anim + 1 >= 16:
            self.anim = 0   
        self.anim += 1
        


    def ataque(self,lista):
        for i in lista:
            colide = self.colisaoProjetil(i)
            if colide:
                i.hit('dano')
                



    def colisaoProjetil(self,alvo) -> bool:
        if self.nome == 'Heitor': 
            return ((self.y+10 - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
                self.y+10 + self.raio>alvo.hitbox[1]) and 
                (self.x+25 + self.raio>alvo.hitbox[0] and 
                self.x+25 - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
                ))
        else:
            return ((self.y - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + self.raio>alvo.hitbox[1]) and 
            (self.x + self.raio>alvo.hitbox[0] and 
            self.x - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))

    def distancia(self,jogador) -> bool:    
        distancia = math.sqrt(((self.x - jogador.x)**2) +
                                ((self.y- jogador.y)**2))
        return distancia > 250
