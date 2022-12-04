import pygame as pg

from Configs import *
from Projeteis import Projetil
import sys
from Inimigos import Inimigo
from Imagens import Imagem
#from Sons import Sons


class Game:
    def __init__(self,tela,jogadores):

        self.FPS_CLOCK = pg.time.Clock()
        self.tela = tela
        #self.jogador = Jogador(posXY=( Player_x, Player_y),posWH = (32,32),personagem=)
        self.jogador1 = jogadores[0]
        self.jogador2 = jogadores[1]
        self.melee = []
        self.projeteis = []
        self.encerrada = False
        self.Inimigo1 = Inimigo(posXY=(991,350),posWH =(32,32),personagem=Soldadinho)
        self.contador = 0
        self.background = Imagem.Background
        self.estruturas = Imagem.Estruturas
        self.lista = Imagem.ListaColisoes
        self.mov = False

    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.colisoes(self.lista)
            self.desenha(self.tela)     
               


    def tratamento_eventos(self):
        mouse_x,mouse_y = pg.mouse.get_pos()         
        self.movimentos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()    
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:        
                self.encerrada = True
                setup.NumTela = 2
                setup.Jogadores.clear()

            #tratamento dos ataques
            #teclas de ataque básico
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                if self.jogador1.cooldown1 >= 15:
                    self.jogador1.ataque(self.tela,self.Inimigo1)

            if event.type == pg.KEYDOWN and event.key == pg.K_e:
                if self.jogador1.cooldown2 >= 30:
                    self.jogador1.ataque_especial(self.tela,self.Inimigo1)
                    
            if event.type == pg.KEYDOWN and event.key == pg.K_u:
                if self.jogador2.cooldown1 >= 15:
                    self.jogador2.ataque(self.tela,self.Inimigo1)
            if event.type == pg.KEYDOWN and event.key == pg.K_o:
                if self.jogador2.cooldown2 >= 30:
                    self.jogador2.ataque_especial(self.tela,self.Inimigo1)
                    

            #Teclas de habilidades especiais

        for projetil in self.jogador1.projeteis:
            if projetil.colisaoProjetil(self.Inimigo1) and self.Inimigo1.visible:
                self.Inimigo1.hit()
                self.jogador1.projeteis.pop(self.jogador1.projeteis.index(projetil))
        for projetil in self.jogador2.projeteis:
            if projetil.colisaoProjetil(self.Inimigo1) and self.Inimigo1.visible:
                self.Inimigo1.hit()
                self.jogador2.projeteis.pop(self.jogador2.projeteis.index(projetil))
            
        
            

        


    
    def desenha(self,tela):
        # mapa

        for i in self.background:
            i.desenha(tela)


        for i in self.estruturas:
           i.desenha(tela)


        self.contador +=1
        if self.contador +1 >= 176:
            self.contador = 0
        self.tela.blit(Imagem.Centro[self.contador//5],(593,234))
    
        

        #desenho jogadores / inimigos
        self.Inimigo1.desenhar(tela)
        self.jogador1.desenhar(tela) 
        self.jogador2.desenhar(tela) 
        
        
        #Desenho projeteis
        '''for projeteis in self.jogador1.projeteis:      
                projeteis.desenha(tela)
        for projeteis in self.jogador2.projeteis:      
                projeteis.desenha(tela)'''
                
        
        #ultimo setup
        pg.display.update()
        self.FPS_CLOCK.tick(30)

    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela

        
        if not self.jogador1.atk and not self.jogador1.atkEspecial:

            if pg.key.get_pressed()[pg.K_a] and (self.jogador1.X > 0) :
                self.jogador1.esquerda()
                self.jogador1.mov_vx = -1

            if pg.key.get_pressed()[pg.K_d] and (self.jogador1.X + 64 < S_WIDHT) :          
                self.jogador1.direita()
                self.jogador1.mov_vx = 1

            if pg.key.get_pressed()[pg.K_w] and (self.jogador1.Y > 0) : 
                self.jogador1.cima()   
                self.jogador1.mov_vy = -1                
                      
            if pg.key.get_pressed()[pg.K_s] and (self.jogador1.Y + 64 < S_HEIGHT) :
                self.jogador1.baixo()
                self.jogador1.mov_vy = 1
            
            #Movimento jogador 2
        if not self.jogador2.atk and not self.jogador2.atkEspecial:
            if pg.key.get_pressed()[pg.K_j] and (self.jogador2.X > 0) :
                self.jogador2.esquerda()
                self.jogador2.mov_vx = -1               

            if pg.key.get_pressed()[pg.K_l] and (self.jogador2.X + 64 < S_WIDHT) :          
                self.jogador2.direita()
                self.jogador2.mov_vx = 1          

            if pg.key.get_pressed()[pg.K_i] and (self.jogador2.Y > 0) : 
                self.jogador2.cima()   
                self.jogador2.mov_vy = -1
                                              
            if pg.key.get_pressed()[pg.K_k] and (self.jogador2.Y + 64 < S_HEIGHT) :
                self.jogador2.baixo()
                self.jogador2.mov_vy = 1
                

        #trata movimento do inimigo
        self.Inimigo1.movimento(self.jogador1,self.jogador2)


    def colisoes(self,lista):
        self.jogador1.colisao(lista)
        self.jogador2.colisao(lista)
        self.Inimigo1.colisao(lista)


        
                




    #800x 600y

    


        
        

        