import pygame as pg

from Configs import Config
from TelaInicial import PrimeiraTela


class Jogo:
    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode((Config.S_WIDHT, Config.S_HEIGHT))
        self.encerrada = False

    pg.display.set_caption('New Land, a adventure RPG')
    #pg.display.set_icon()

    def rodar(self):
        Config.Tela = 1
        while True:
            if Config.Tela == 1:
                NovaTela = PrimeiraTela(self.tela)
                NovaTela.rodar()