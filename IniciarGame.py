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
        self.jogador = jogadores[0]
        
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
        self.movimentos()
        
        mouse_x,mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()            
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    self.projeteis.append(Projetil(self.jogador.X+32,self.jogador.Y+45,5,mouse_x,mouse_y))              
                    #Sons.BarulhoProjetil(self)
        #for jogador in self.jogadores:
        #    if jogador.disparo():
        #        pass     
        for projetil in self.projeteis:
            if projetil.colisaoProjetil(self.Inimigo1) and self.Inimigo1.visible:
                self.Inimigo1.hit()
                self.projeteis.pop(self.projeteis.index(projetil))
            

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.encerrada = True
    
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
        self.jogador.desenhar(tela) 
        self.Inimigo1.desenhar(tela)
        
        #Desenho projeteis
        for projeteis in self.projeteis:      
                projeteis.desenha(tela)
                
                projeteis.atk = True
                
        
        #ultimo setup
        pg.display.update()
        self.FPS_CLOCK.tick(30)

    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela
        
        if not self.jogador.atk:
            if pg.key.get_pressed()[pg.K_a] and (self.jogador.X > 0) :
                self.jogador.esquerda()
                self.jogador.mov_esquerda = True

            if pg.key.get_pressed()[pg.K_d] and (self.jogador.X + 64 < S_WIDHT) :          
                self.jogador.direita()
                self.jogador.mov_direita = True

            if pg.key.get_pressed()[pg.K_w] and (self.jogador.Y > 0) : 
                self.jogador.cima()   
                self.jogador.mov_cima = True                 
                      
            if pg.key.get_pressed()[pg.K_s] and (self.jogador.Y + 64 < S_HEIGHT) :
                self.jogador.baixo()
                self.jogador.mov_baixo = True



    def colisoes(self,lista):
        self.jogador.colisao(lista)
        
                




    #800x 600y

    


        
        

        