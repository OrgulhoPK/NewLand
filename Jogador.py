import pygame as pg
from Imagens import Imagem

from Personagens import Personagem
class Jogador:
    def __init__(self,posxy,personagem:Personagem): #(self, x, y, widht, height)
        #posição e speed
        self.x = posxy[0]
        self.y = posxy[1]
        self.mov_vx = 0
        self.mov_vy = 0
        self.speed = 4
        #Dados dos inimigos
        self.dados = []   
        #Atributos e skills de personagens
        #separei para ter uma visao melhor dos atributos
        self.nome = personagem.nome
        self.vida = personagem.vida
        self.hpmax = personagem.vida #orientacao para barra hp e heal
        self.dano = personagem.dano
        self.hitbox = pg.Rect(self.x+17,self.y+34,31,31)
        self.sprites = personagem.sprites
        self.HBasica = personagem.habilidade[0]
        self.HEspecial = personagem.habilidade[1]
        self.projeteis = []  #list projeteis
        #estado e  condições
        self.mousexy = None  #posicao do mouse para habilidade
        self.visible= True
        self.atk = False
        self.atkEspecial = False
        self.acao = True     
        self.mouse = False
         #controle de grupo
        self.slow = False
        self.stun = False
        self.timestun = 0 
        self.timeslow = 0
        self.status = self.speed
        #Contadores de animação e  efeitos
        self.cooldown1= 0
        self.cooldown2= 0
        self.sequenciaATK = 0
        self.anim_mov = 0    
        self.countatk = 0
        self.countspec =  0

    #speed do jogador
    def esquerda(self):
        self.x -= self.speed
    def direita(self):
        self.x += self.speed
    def cima(self):
        self.y -= self.speed
    def baixo(self):
        self.y  += self.speed
    def parar(self):
        self.mov_vy = 0
        self.mov_vx = 0

    #Função que calcula colisão com uma lista de objetos
                    
    def ataque(self,tela,alvo,Totem):
        dados = alvo + Totem
        self.dados= [tela,dados]
        self.atk = True

    def ataque_especial(self,tela,alvo,Totem,jogador = None):
        dados = Totem+alvo
        self.dados= [tela,dados,jogador]
        self.atkEspecial = True
    #controles de grupo     
    def atualizarEstado(self,tela):
        if self.stun:  
            if self.timestun+1 >=60:
                self.timestun = 0
                self.stun = False
            tela.blit(Imagem.starStun1[self.timestun//5],(self.x+5,self.y-5))
            self.timestun +=1

        if self.slow:
            if self.timeslow == 0:
                self.status = self.speed
            if self.timeslow+1 >=60:
                self.timeslow = 0
                self.slow = False
            self.speed = self.status/2
            self.timeslow +=1
        if not self.slow:
            self.speed = self.status

    def hit(self):
        if self.vida>0:
            self.vida -=1
        else:
            self.visible = False

    def colisao(self,alvo):
        if self.visible:
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

    def getMouse(self):
        for event in pg.event.get():
            mousexy = None
            mx,my = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    mousexy = (mx,my)
                    self.mouse = False
                    return mousexy

    def desenhar(self,tela):
        #sprites
        esq_Dir,cima,baixo,ataque,especial = self.sprites[0],self.sprites[1],self.sprites[2],self.sprites[3],self.sprites[4]
        #Contador de animação (desenho)
        if self.visible:
            if self.anim_mov+1 >= 28:
                self.anim_mov = 0
            self.anim_mov +=1

            #ataques básicos
            if self.atk:
                #Duelista
                if self.nome == 'Ida':            
                    if self.mov_vx == -1:
                        if self.countatk == 13:
                            self.HBasica.Basica(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy))
                        tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x-64,self.y-64))
                    else:
                        if self.countatk == 13:
                            self.HBasica.Basica(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy))
                        tela.blit(ataque[self.countatk//2],(self.x-64,self.y-64))
                    
                    if self.countatk +1 >= 16:
                        self.countatk = 0
                        self.atk = False
                        self.cooldown1 = 0
                    self.countatk +=1
                #Tanker
                if self.nome == 'Guaraci':            
                    if self.mov_vx == -1:
                        if self.countatk >10: 
                            self.x -= self.speed*1.5
                            tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x,self.y))
                        if self.countatk == 15:
                                self.HBasica.BasicaGuaraci(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy),self.speed)
                        tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x,self.y))
                    else:
                        if self.countatk >10: 
                            self.x += self.speed*1.5
                        if self.countatk == 15:
                            self.HBasica.BasicaGuaraci(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy),self.speed)
                            
                        
                        tela.blit(ataque[self.countatk//2],(self.x,self.y))
                    
                    if self.countatk +1 >= 16:
                        self.countatk = 0
                        self.cooldown1 = 0
                        self.atk = False
                        
                    self.countatk +=1

                #Clerigo e Shaman
                if self.nome == 'Heitor' or self.nome == 'Jurupari': 

                    if self.mov_vx == -1:
                        tela.blit(pg.transform.flip(ataque[self.countatk//2],True,False),(self.x,self.y))
                    else:
                        tela.blit(ataque[self.countatk//2],(self.x,self.y))  
                                                     
                    if self.countatk +1 >= 16:
                        self.countatk = 0
                        self.atk = False
                        projetil = self.HBasica.BasicaRange(self.nome,self.x,self.y,(self.mov_vx,self.mov_vy))
                        self.projeteis.append(projetil) 
                        self.cooldown1 = 0
                        
                        

                    self.countatk +=1

            #ataques especiais
            if self.atkEspecial:
                #Duelista
                if self.nome == 'Ida':
                    if self.mov_vx == -1:
                        if self.countspec >10:
                            self.x -= self.speed*1.5
                            self.HEspecial.EspecialD(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy))
                        tela.blit(pg.transform.flip(especial[self.countspec//2],True,False),(self.x-64,self.y-64))
                    else:

                        if self.countspec > 10:
                            self.x += self.speed*1.5
                            self.HEspecial.EspecialD(self.x,self.y,self.dados,(self.mov_vx,self.mov_vy))
                        tela.blit(especial[self.countspec//2],(self.x-64,self.y-64))
                
                    if self.countspec +1 >= 23:
                        self.countspec = 0
                        self.atkEspecial = False
                        self.cooldown2 = 0
                    self.countspec +=1
                #Clerigo
                if self.nome == 'Heitor':
                    if self.countspec < 45:
                        pg.draw.circle(tela,(254,250,182),(self.x+32,self.y+32),90,1)
                        pg.draw.circle(tela,(254,250,182),(self.x+32,self.y+32),90-self.countspec*2,1)
                        tela.blit(especial[self.countspec//5],(self.x,self.y))                        
                    
                    if self.countspec+1 >=45:
                        tela.blit(especial[self.countspec//7],(self.x,self.y))
                        self.HEspecial.EspecialH(self.x,self.y,self.dados)
                        self.countspec = 0
                        self.atkEspecial = False
                        self.cooldown2 = 0                
                    self.countspec+=1
                #Shaman
                if self.nome == 'Jurupari':
                    if self.mouse:  
                        tela.blit(especial[8],(self.x,self.y))
                        self.mousexy = self.getMouse()
                    if not self.mouse:  
                        if self.countspec <45:
                            pg.draw.circle(tela,(255,0,0),(self.mousexy[0],self.mousexy[1]),self.countspec*2,1)
                            tela.blit(especial[self.countspec//5],(self.x,self.y))
                        elif self.countspec <135:
                            pg.draw.circle(tela,(255,0,0),(self.mousexy[0],self.mousexy[1]),92,2)
                            self.HEspecial.EspecialJ(self.mousexy,self.dados)
                            tela.blit(especial[self.countspec//15],(self.x,self.y))
                        if self.countspec +1 >= 136:
                            self.countspec = 0
                            self.atkEspecial = False
                            self.mousexy = None
                            self.cooldown2 = 0
                        self.countspec+=1
                if self.nome == 'Guaraci':
                    if self.countspec>7:
                        self.HEspecial.EspecialG(self.dados,self)

                    tela.blit(especial[self.countspec//2],(self.x,self.y))
                    if self.countspec +1 >= 16:
                        self.countspec = 0
                        self.atkEspecial = False
                        self.mousexy = None
                        self.cooldown2 = 0
                    self.countspec+=1


            #movimentacao do jogador
            if not self.atk and not self.atkEspecial:
                if self.mov_vx == 0 and self.mov_vy ==0:
                    tela.blit(pg.transform.scale(baixo[0], (64,64)),(self.x,self.y))

                elif self.mov_vx == 1 or (self.mov_vx ==1 and 
                    (self.mov_vy == 1 or self.mov_vy == -1)):                
                    tela.blit(pg.transform.scale(esq_Dir[self.anim_mov//4], (64,64)),(self.x,self.y))


                elif self.mov_vx == -1 or (self.mov_vx == -1 and
                    (self.mov_vy == 1 or self.mov_vy == -1)):   
                    tela.blit(pg.transform.scale(pg.transform.flip(esq_Dir[self.anim_mov//4],True,False), (64,64)),(self.x,self.y))


                elif self.mov_vy == -1:
                    tela.blit(pg.transform.scale(cima[self.anim_mov//4], (64,64)),(self.x,self.y))  


                elif self.mov_vy == 1:
                    tela.blit(pg.transform.scale(baixo[self.anim_mov//4], (64,64)),(self.x,self.y))

                self.parar()  
            #projeteis
            for projeteis in self.projeteis:      
                projeteis.desenha(tela)  

            self.cooldown1 += 1
            self.cooldown2 += 1

            #atualizar posicao do hitbox e barra de vida
            self.hitbox = pg.Rect(self.x+17,self.y+34,31,31)
            pg.draw.rect(tela,(255,0,0),(self.x+17,self.y,40,8))
            pg.draw.rect(tela,(0,128,0),(self.x+17,self.y,((self.vida/self.hpmax)*40),8))



    
