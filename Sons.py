from pathlib import Path
import pygame as pg


class Sons:
    def BarulhoProjetil(self):
        #caminho = Path(__file__)
        pg.mixer.init()

        barulho = pg.mixer.Sound('whoosh.ogg')
        som = barulho.play()


    def MusicaTelaInicial(self):
        #caminho = Path(__file__)
        pg.mixer.init()
        menu1 = pg.mixer.Sound('menu1.ogg')
        somMenu1 = menu1.play()