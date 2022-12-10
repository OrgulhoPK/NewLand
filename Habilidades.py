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
        self.speed = 0.5
        self.contador = 0
        self.pos = 0    #serve somente para contar uma nova posição para o x e y
        self.sprite= sprites

        #contador para time debuff
        self.time_efeito = 0
        self.tempo = 0

#Mob e Duelista
    def Basica(self,x,y,dados,velxy):#Ataque mob e duelista
        
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
                if alvo.nome == 'Soldado' or alvo.nome == 'Boss':
                    alvo.hit(6)
                else:
                    alvo.hit(2)
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
                alvo.hit(4)
                self.contador+=1

#Clerigo e Shaman     
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
                alvo.hit(25)
                alvo.stun = True
                if self.contador+1 >=5:
                    self.contador = 0
                self.contador+=1
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
                alvo.hit(1)

                self.contador+=1

#Tanker
    def BasicaGuaraci(self,x,y,dados,velxy,mov): #Ataque Tanker
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
                alvo.hit(10)
                alvo.stun = True
    def EspecialG(self,dados,jogador): #Especial Tanker
        tela = dados[0]
        if jogador.vida < jogador.hpmax:
            jogador.vida += 3
        tela.blit(pg.transform.scale(self.sprite,(72,64)),(jogador.x-5,jogador.y+25))

#Terreno e Totem
    def Teleporte(self,tela,aliados,inimigos):
        listTarget = aliados + inimigos
        self.time_efeito+= 1
        if self.time_efeito>300:
            if self.time_efeito==301:
                self.x = random.randint(126,1105)
                self.y = random.randint(292,563)   
            tela.blit(pg.transform.scale(self.sprite[self.contador//4],(64,40)),(self.x-30,self.y))
            #pg.draw.circle(tela,(0,0,0),(self.x,self.y+24),self.raio,2)
            #pg.draw.circle(tela,(55,28,15),(self.x,self.y+24),self.raio*20,2)
            for i in listTarget:
                if self.colisao(i,(self.raio*20)) and i.visible:
                    self.seguir(i)
                if self.colisao(i,(self.raio)) and i.visible:
                    if self.tempo == 15:
                        self.time_efeito = 0
                        self.tempo = 0
                        i.x = random.randint(126,1105)
                        i.y = random.randint(292,563)  
                    self.tempo +=1
                               
            self.contador +=1
            if self.contador +1 >=16:
                self.contador = 0                
    def Slow(self,tela,aliados,inimigos):
        listTarget = aliados + inimigos
        self.time_efeito+= 1
        if self.time_efeito>180:
            if self.time_efeito==181:
                self.x = random.randint(126,1105)
                self.y = random.randint(292,563)   
            tela.blit(pg.transform.scale(self.sprite[self.contador//4],(64,40)),(self.x-30,self.y))
            for i in listTarget:
                if self.colisao(i,(self.raio*20)) and i.visible:
                    self.seguir(i)
                if self.colisao(i,(self.raio)) and i.visible:
                    if self.tempo == 15:
                        self.time_efeito = 0
                        self.tempo = 0
                        i.slow = True
                    self.tempo +=1
                               
            self.contador +=1
            if self.contador +1 >=16:
                self.contador = 0            
    def cura(self,x,y,tela,dados):
        self.x = x+12
        self.y = y+54
        tela.blit(pg.transform.scale(self.sprite,(110,100)),(self.x-54,self.y-48))
        if self.contador>=30:
            self.contador = 0
            for i in dados:
                if self.colisao(i,self.raio):
                    if i.vida < i.hpmax:
                        i.vida +=2
        self.contador+=1

            
        self.contador+=1 

#Complemento de algumas skills
    def colisao(self,alvo, raio) -> bool:
        return ((self.y - raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + raio>alvo.hitbox[1]) and 
            (self.x + raio>alvo.hitbox[0] and 
            self.x - raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))
    def seguir(self,alvo):
        #objeto segue o personagem 
        #pode ser aplicado para qualquer skill basica ou terreno móvel
        alvo_x= alvo.x + 32
        alvo_y= alvo.y + 32
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
        return distancia > 350
