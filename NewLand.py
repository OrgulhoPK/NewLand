import pygame as pg

from Configs import Config
from TelaInicial import PrimeiraTela
from TelaSelecao import TelaSelecao
from IniciarGame import Game
from Sons import Sons


class Jogo:
    def __init__(self):
        pg.init()
        self.tela = Config.tela
        self.encerrada = False

    pg.display.set_caption('New Land, a adventure RPG')
    #pg.display.set_icon()

    def rodar(self):
        Config.Telas = 1
        while True:
            if Config.Telas == 1:
                Sons.menu1.play() 
                NovaTela = PrimeiraTela(self.tela)
                NovaTela.rodar()
            if Config.Telas == 2:
                NovaTela = TelaSelecao(self.tela)
                NovaTela.rodar()
            if Config.Telas == 3:
                NovaTela1 = Game(self.tela,Config.Jogadores)
                NovaTela1.rodar()