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

    pg.display.set_caption('New Land, a adventure RPG')
    #pg.display.set_icon()

    def rodar(self):
        setup.NumTela = 1
        while True:
            if setup.NumTela == 1:
                Sons.menu1.play() 
                NovaTela = PrimeiraTela(self.tela)
                NovaTela.rodar()
            if setup.NumTela == 2:
                NovaTela = TelaSelecao(self.tela)
                NovaTela.rodar()
            if setup.NumTela == 3:
                NovaTela1 = Game(self.tela,setup.Jogadores)
                NovaTela1.rodar()

            