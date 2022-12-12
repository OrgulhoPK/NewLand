import pygame as pg

from Configs import *
from TelaInicial import PrimeiraTela
from TelaSelecao import TelaSelecao
from IniciarGame import Game
from Sons import Sons


class Jogo:
    def __init__(self):
        pg.init()
        self.tela = tela
        self.Fase = setup()

    pg.display.set_caption('New Land, a adventure RPG')
    #pg.display.set_icon()
    

    def rodar(self):
        self.Fase.NumTela = 1
        while True:
            if self.Fase.NumTela == 1:
                Sons.menu1.play() 
                NovaTela = PrimeiraTela(self.tela,self.Fase)
                NovaTela.rodar()
            if self.Fase.NumTela == 2:
                NovaTela = TelaSelecao(self.tela,self.Fase)
                NovaTela.rodar()
            if self.Fase.NumTela == 3:
                self.Fase.adicionarInimigos()
                NovaTela1 = Game(self.tela,self.Fase)
                NovaTela1.rodar()

            