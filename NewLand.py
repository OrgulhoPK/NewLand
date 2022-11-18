import pygame as pg

from Configs import Config
from TelaInicial import PrimeiraTela
from IniciarGame import Game
#from Sons import Sons


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
                #Sons.menu1.play() 
                NovaTela = PrimeiraTela(self.tela)
                NovaTela.rodar()
            if Config.Tela == 2:
                NovaTela1 = Game(self.tela)
                NovaTela1.rodar()