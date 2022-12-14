import pygame as pg
import math
from Imagens import Imagem
from Personagens import Personagem


class Inimigo: 
    def __init__(self,posxy:list[float],personagem:Personagem):
        #posicao e speed
        self.x = posxy[0]
        self.y = posxy[1]
        self.inimigovx = 0
        self.inimigovy = 0
        self.speed = personagem.speed
        #dados de jogadores
        self.dados = []
        #Atributos e skills de personagens
        self.nome = personagem.nome
        self.vida = personagem.vida
        self.hpmax = personagem.vida #orientacao para barra hp e heal
        self.hitbox = pg.Rect(self.x+17,self.y+34,31,31)
        self.sprites = personagem.sprites
        self.HBasica = personagem.habilidade[0]
        self.HEspecial = personagem.habilidade[1]
        self.projeteis = []  #list projeteis
        self.summons = [] #lista para invocar mais 'aliados'
        #estado e condiçoes
        self.atk = False
        self.atkEspecial = False
        self.visible= True
        self.acao = True
        #controle de grupo
        self.stun = False
        self.slow = False
        self.timestun = 0
        self.timeslow = 0
        self.status = 1  # orientacao para o speed
        #Contadores de animacao e efeitos
        self.anim_mov = 0
        self.countatk = 0
        self.countspec= 0
        self.cooldown1= 0
        self.cooldown2= 0
        self.timestun = 0

    def seguir(self,jogador:list):
        alvo_x= jogador.x+32
        alvo_y= jogador.y 
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

    def movimento(self,jogador1,jogador2):
        if self.nome == 'Estrutura':
            self.inimigovx = 1
            self.inimigovy = 1
        else:
            distancia1 = math.sqrt(((self.hitbox.centerx - jogador1.hitbox.centerx)**2) +
                                    ((self.hitbox.centery- jogador1.hitbox.centery)**2))

            distancia2 = math.sqrt(((self.hitbox.centerx - jogador2.hitbox.centerx)**2) +
                                    ((self.hitbox.centery- jogador2.hitbox.centery)**2))

            if distancia1 < distancia2:
                if jogador1.visible:
                    self.seguir(jogador1)
                elif jogador2.visible:
                    self.seguir(jogador2)        
            else:
                if jogador2.visible:
                    self.seguir(jogador2)
                elif jogador1.visible:
                    self.seguir(jogador1)

    def hit(self,dano:int):
        if self.nome == 'Estrutura':
            self.vida -= 1
       
        else:
            if self.vida>0:
                self.vida -= dano            
            else:
                self.visible = False

    def ataque(self,tela,alvo:list):
        self.dados= [tela,alvo]
        self.atk = True

    def ataque_especial(self,tela,alvo:list):
        self.dados= [tela,alvo]
        self.atkEspecial = True
    
    def atualizarEstado(self):
        #controles de grupo 
        if self.stun:  
            if self.timestun+1 >=60:
                self.timestun = 0
                self.stun = False
            self.timestun +=1

        if self.slow:
            if self.timeslow == 0:
                self.status = self.speed
            if self.timeslow+1 >=150:
                self.timeslow = 0
                self.slow = False
                self.speed = self.status
            self.speed = self.status/2
            self.timeslow +=1
        if not self.slow:
            self.speed = self.status

      
    #Definido uma area de ameaça para utilizar os ataques basicos e/ou habilidades
    def areaameaca(self,alvo,raio:int) -> bool:
        return ((self.y+40 - raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y+40 + raio>alvo.hitbox[1]) and 
            (self.x+32 + raio>alvo.hitbox[0] and 
            self.x+32 - raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))
    #"alvo:list" referente a todos os objetos que podem colidir
    def colisao(self,alvo:list):
        collision_tolerance = 10
        for i in alvo:
            colide = self.hitbox.colliderect(i)
            if colide:          
                if abs(i.top - self.hitbox.bottom) < collision_tolerance:
                    self.hitbox.bottom -= collision_tolerance 
                    self.y -= self.speed
                if abs(i.bottom - self.hitbox.top) < collision_tolerance:
                    self.hitbox.top += collision_tolerance 
                    self.y += self.speed
                if abs(i.right - self.hitbox.left) < collision_tolerance:
                    self.hitbox.left += collision_tolerance 
                    self.x += self.speed
                if abs(i.left - self.hitbox.right) < collision_tolerance:
                    self.hitbox.right -= collision_tolerance 
                    self.x -= self.speed

    def desenhar(self,tela):
        if self.nome == 'Estrutura':
            self.desenharEstrutura(tela)
        else:
            esq_Dir = self.sprites[0]
            baixo = self.sprites[2]
            ataque = self.sprites[3]
            especial = self.sprites[4]
            if self.visible:
                if self.atk:
                    if self.nome == 'Soldado' or self.nome == 'Boss':            
                        if self.inimigovx <= 0:
                            if self.countatk == 13:
                                self.HBasica.Basica(self.nome,self.x,self.y,self.dados,(-1,self.inimigovy))
                            tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x-32,self.y-32))
                        else:
                            if self.countatk == 13:
                                self.HBasica.Basica(self.nome,self.x,self.y,self.dados,(self.inimigovx,self.inimigovy))
                            tela.blit(ataque[self.countatk//2],(self.x-32,self.y-32))
                        
                        if self.countatk +1 >= 16:
                            self.countatk = 0
                            self.atk = False
                            self.cooldown1 = 0
                        self.countatk +=1
                if self.anim_mov +1 >= 28:
                    self.anim_mov = 0
                self.anim_mov += 1

                if self.atkEspecial:
                    if self.nome == 'Soldado':
                        if self.inimigovx :
                            tela.blit(especial[self.countspec//4],(self.x-32,self.y-32))  
                        if self.countspec +1 >= 24:
                            self.countspec = 0
                            self.cooldown2 = 0
                            self.atkEspecial = False
                            projetil = self.HEspecial.BasicaRange(self.nome,self.x,self.y,(self.inimigovx,self.inimigovy))
                            self.projeteis.append(projetil)       
                        self.countspec +=1
                    if self.nome == 'Boss':
                        if self.inimigovx :
                            tela.blit(especial[self.countspec//4],(self.x,self.y))                  
                        if self.countspec +1 >= 32:
                            self.countspec = 0
                            self.cooldown2 = 0
                            self.atkEspecial = False
                            inimigo = self.HEspecial.EspecialBoss(self)
                            self.summons.append(inimigo)   
                        self.countspec +=1
                #desenha o mob
                if not self.atk and not self.atkEspecial:
                    if self.inimigovx == 0 and self.inimigovy == 0:
                        tela.blit(pg.transform.scale(baixo[0], (64,64)),(self.x,self.y))
                    
                    elif self.inimigovx>0 or (self.inimigovx>0 and (self.inimigovy>0 or self.inimigovy<0)):                    
                        tela.blit(pg.transform.scale(esq_Dir[self.anim_mov//4], (64,64)),(self.x,self.y))

                    elif self.inimigovx<0 or (self.inimigovx<0 and (self.inimigovy>0 or self.inimigovy<0)):
                        tela.blit(pg.transform.scale(pg.transform.flip(esq_Dir[self.anim_mov//4],True,False), (64,64)),(self.x,self.y))

                if self.stun:
                    tela.blit(Imagem.starStun1[self.timestun//5],(self.x+5,self.y-10))
                #atualiza o hitbox do mob e barra de vida
                self.hitbox = pg.Rect(self.x+17,self.y+34,31,31)
                pg.draw.rect(tela,(255,0,0),(self.x+17,self.y,40,8))
                pg.draw.rect(tela,(0,128,0),(self.x+17,self.y,((self.vida/self.hpmax)*40),8))
                for projeteis in self.projeteis:      
                    projeteis.desenha(tela)
                self.cooldown1 += 1
                self.cooldown2 += 1
    def desenharEstrutura(self,tela):
        objeto = self.sprites[0]
        if self.atk:
            tela.blit(objeto[0],(self.x,self.y))
            if self.countatk <300:
                self.HBasica.cura(self.x,self.y,tela,self.dados)
            if self.countatk +1 >= 840:
                self.countatk = 0
                self.vida = 7
                self.atk = False
            self.countatk +=1 
        if not self.atk:
            if self.vida >0:
                tela.blit(objeto[self.vida],(self.x,self.y))

        if self.vida<=0:
            self.vida = 0
            self.atk = True
        self.hitbox = pg.Rect(self.x,self.y+33,28,35)


        
