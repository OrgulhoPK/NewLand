import pygame as pg
import sys

from Configs import Config

class TelaSelecao:
    def __init__(self,tela):
        self.tela = tela
        self.encerra = False
        self.FPS_Clock = pg.time.Clock()
        self.contador = 0
        self.opcoes = Config.TelaInicial
        self.menu = 0
    
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.SelectMenu()
            self.desenha(self.tela)
        

    def tratamento_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit()
                pg.quit()

    