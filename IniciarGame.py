
import pygame as pg

from Configs import Config
from Jogador import Jogador
from Projeteis import Projetil
import sys
from Inimigos import Inimigos


class Game:
    def __init__(self):
        pg.init()
        self.FPS_CLOCK = pg.time.Clock()
        self.tela = pg.display.set_mode((Config.S_WIDHT,Config.S_HEIGHT))
        self.jogador = Jogador(posXY=(Config.Player_x,Config.Player_y),posWH = (32,32))
        self.projeteis = []
        self.encerrada = False
        self.Inimigos = Inimigos(posXY=(500,300),posWH = (32,32))


    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()         


    def atualiza_estado(self):
        self.jogador.atualizar_posicao()

    def tratamento_eventos(self):         
        self.movimentos()
        #self.colisoes()
        mouse_x,mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    self.projeteis.append(Projetil(self.jogador.posXY[0]-self.jogador.scroll[0]+32,self.jogador.posXY[1]-self.jogador.scroll[1]+32,mouse_x,mouse_y))


        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.encerrada = True
    
    def desenha(self):
        self.tela.fill((Config.COR_Tela))
        for projeteis in self.projeteis:
                projeteis.desenha(self.tela) 
        self.jogador.desenhar(self.tela) 
        self.Inimigos.desenhar(self.tela)
        pg.display.flip()
        self.FPS_CLOCK.tick(30)

    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela
        if pg.key.get_pressed()[pg.K_a] and (self.jogador.posXY[0] - self.jogador.scroll[0]>0) :
            self.jogador.esquerda()
            self.jogador.mov_esquerda = True
        if pg.key.get_pressed()[pg.K_d] and (self.jogador.posXY[0] - self.jogador.scroll[0] + 64 < Config.S_WIDHT):          
            self.jogador.direita()
            self.jogador.mov_direita = True
        if pg.key.get_pressed()[pg.K_w] and (self.jogador.posXY[1] - self.jogador.scroll[1]>0):
            self.jogador.cima()   
            self.jogador.mov_cima = True                                       
        if pg.key.get_pressed()[pg.K_s] and (self.jogador.posXY[1] - self.jogador.scroll[1] + 64 < Config.S_HEIGHT):
            self.jogador.baixo()
            self.jogador.mov_baixo = True

            


    #800x 600y

    def colisoes(self):
        '''if self.jogador.posXY[0] < 0:
            self.jogador.movimento = 0
        if self.jogador.posXY[1] < 0:
            self.jogador.posXY[1]= 0
        if self.jogador.right > Config.S_WIdwDHT:
            self.jogador.right = Config.S_WIDHT
        if self.jogador.top <= 0:
            self.jogador.top = 0
        if self.jogador.bottom >= Config.S_HEIGHT:
            self.jogador.bottom = Config.S_HEIGHT'''

        