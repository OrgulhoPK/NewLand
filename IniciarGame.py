import pygame as pg

from Configs import Config
from Jogador import Jogador
from Projeteis import Projetil
import sys
from Inimigos import Inimigos
from Imagens import Imagem
from Sons import Sons


class Game:
    def __init__(self,tela):
        pg.init()
        self.FPS_CLOCK = pg.time.Clock()
        self.tela = tela
        self.jogador = Jogador(posXY=(Config.Player_x,Config.Player_y),posWH = (32,32))
        self.jogadores = []
        
        self.projeteis = []
        self.encerrada = False
        self.Inimigo1 = Inimigos(posXY=(750,400),posWH = (32,32))
        self.contador = 0
        self.background = Imagem.Background
        self.estruturas = Imagem.Estruturas
        self.lista = Imagem.ListaColisoes
        self.mov = True

    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.colisoes(self.lista)
            self.desenha(self.tela)         


    def atualiza_estado(self):
        self.jogador.atualizar_posicao()

    def tratamento_eventos(self):         
        self.movimentos()
        
        mouse_x,mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()            
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    self.projeteis.append(Projetil(self.jogador.X+32,self.jogador.Y+45,5,mouse_x+1,mouse_y))              
                    Sons.BarulhoProjetil(self)
        #for jogador in self.jogadores:
        #    if jogador.disparo():
        #        pass
         
        for projetil in self.projeteis:
            if projetil.colisaoProjetil(self.Inimigo1):
                self.Inimigo1.dano()
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


        for i in self.lista:
            pg.draw.rect(tela,Config.COR_Tela,i,2) 

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

        if not self.jogador.atk and not(self.mov) :
            if pg.key.get_pressed()[pg.K_a] and (self.jogador.X >0) :
                self.jogador.esquerda()
                self.jogador.mov_esquerda = True

            if pg.key.get_pressed()[pg.K_d] and (self.jogador.X + 64 < Config.S_WIDHT) :          
                self.jogador.direita()
                self.jogador.mov_direita = True

            if pg.key.get_pressed()[pg.K_w] and (self.jogador.Y > 0) : 
                self.jogador.cima()   
                self.jogador.mov_cima = True                 
                      
            if pg.key.get_pressed()[pg.K_s] and (self.jogador.Y + 64 < Config.S_HEIGHT) :
                self.jogador.baixo()
                self.jogador.mov_baixo = True
        self.mov = False


    def colisoes(self,lista):
        for i in lista:
            if self.jogador.colisao(i):
                print('colidiu')
                self.mov = True



    #800x 600y

    


        
        

        