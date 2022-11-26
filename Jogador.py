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
        self.nome = personagem.nome
        self.vida = personagem.vida
        self.dano = personagem.dano
        #referente ao personagem vivo ou nao
        self.visible= True
        self.sprites = personagem.sprites
        self.habilidade = personagem.habilidade
        self.cooldown1= 0
        self.cooldown2= 0

        #referente à animação do personagem    
        self.anim_mov = 0    #é só um contador de animação (trocar o frame)
        self.countatk = 0    #contador animacao ataque 
        self.mov_vx = 0
        self.mov_vy = 0
        self.atk = False
        self.dados = []
        #referente ao uso de habilidades
        self.sequenciaATK = 0

        #hitbox = X, Y , Largura, Altura  Rect()
        self.hitbox = pg.Rect(self.X+17,self.Y+34,31,31)

    #criar funções para movimentar o jogador
    def esquerda(self):
        self.X -= self.movimento
    def direita(self):
        self.X += self.movimento
    def cima(self):
        self.Y -= self.movimento
    def baixo(self):
        self.Y  += self.movimento
    def parar(self):
        self.mov_vy = 0
        self.mov_vx = 0

    #Função que calcula colisão com uma lista de objetos
    def colisao(self,alvo):
        collision_tolerance = 10
        for i in alvo:
            colide = self.hitbox.colliderect(i)
            if colide:          
                if abs(i.top - self.hitbox.bottom) < collision_tolerance:
                    self.hitbox.bottom -= collision_tolerance 
                    self.cima()
                if abs(i.bottom - self.hitbox.top) < collision_tolerance:
                    self.hitbox.top += collision_tolerance 
                    self.baixo()
                if abs(i.right - self.hitbox.left) < collision_tolerance:
                    self.hitbox.left += collision_tolerance 
                    self.direita()  
                if abs(i.left - self.hitbox.right) < collision_tolerance:
                    self.hitbox.right -= collision_tolerance 
                    self.esquerda()
                    

                        

    def disparo(self):
        pass

    def ataque(self,tela,alvo):
        self.dados= [tela,alvo]
        self.atk = True
        

    def hit(self):
        if self.vida>0:
            self.dano = True
            self.vida -=1
        else:
            self.visible = False




    def desenhar(self,tela):
        esq_Dir = self.sprites[0]
        cima = self.sprites[1]
        baixo = self.sprites[2]
        ataque = self.sprites[3]
        #pg.draw.circle(tela,(0,0,0),(self.X+70,self.Y+35),40)
        #pg.draw.ellipse(tela, (0,0,0), [self.X+32,self.Y+20, 80, 40])
        pg.draw.rect(tela,(255,100,2),[self.X+32,self.Y+20, 27, 35])
        #Contador de animação (desenho)
        if self.visible:
            if self.anim_mov+1 >= 28:
                self.anim_mov = 0
            self.anim_mov +=1

            #Tratamento da animação de ataque
            #if pg.mouse.get_pressed()[0] :
            #    self.atk = True
            if self.atk:
                self.cooldown1 = 0   
                
                if self.nome == 'Ida' or self.nome == 'Soldadinho':
                    if self.countatk +1 >= 25:
                        self.countatk = 0
                        self.atk = False
                        self.dados.clear()
                    
                    if self.countatk +1 >= 15:
                        self.X += self.movimento*3
                        self.habilidade.Basica(self.X,self.Y,self.dados)
                        tela.blit(ataque[self.countatk//2],(self.X-64,self.Y-64))
                    else:
                        tela.blit(ataque[self.countatk//2],(self.X-64,self.Y-64))
                else:
                    if self.countatk +1 >= 33:
                        self.countatk = 0
                        self.atk = False
                        self.dados.clear()
                    tela.blit(pg.transform.scale(ataque[self.countatk//4], (64,64)),(self.X,self.Y))
                
                self.countatk +=1
                print((self.countatk))
            

            if not self.atk:
                if self.mov_vx == 0 and self.mov_vy ==0:
                    tela.blit(pg.transform.scale(baixo[0], (64,64)),(self.X,self.Y))

                elif self.mov_vx == 1 or (self.mov_vx ==1 and 
                    (self.mov_vy == 1 or self.mov_vy == -1)):                
                    tela.blit(pg.transform.scale(esq_Dir[self.anim_mov//4], (64,64)),(self.X,self.Y))


                elif self.mov_vx == -1 or (self.mov_vx == -1 and
                    (self.mov_vy == 1 or self.mov_vy == -1)):   
                    tela.blit(pg.transform.scale(pg.transform.flip(esq_Dir[self.anim_mov//4],True,False), (64,64)),(self.X,self.Y))


                elif self.mov_vy == -1:
                    tela.blit(pg.transform.scale(cima[self.anim_mov//4], (64,64)),(self.X,self.Y))  


                elif self.mov_vy == 1:
                    tela.blit(pg.transform.scale(baixo[self.anim_mov//4], (64,64)),(self.X,self.Y))
                
                self.parar()
                self.cooldown1 += 1


                



            #atualizar posicao do hitbox
            self.hitbox = pg.Rect(self.X+17,self.Y+34,31,31)
            
            pg.draw.rect(tela,COR_Tela,self.hitbox,2)
            pg.draw.rect(tela,(255,0,0),(self.X+17,self.Y,40,8))
            pg.draw.rect(tela,(0,128,0),(self.X+17,self.Y,40 - (4 * (10-self.vida)),8))
