from pathlib import Path
import pygame as pg


class Sons:
    pg.mixer.init()


    ##Chamando a musica menu
    menu1 = pg.mixer.Sound('menu1.ogg')

    valor = menu1.set_volume(1.0)
    
    
    
    
    
    def BarulhoProjetil(self):
        #caminho = Path(__file__)
        pg.mixer.init()
        barulho = pg.mixer.Sound('whoosh.ogg')
        som = barulho.play()


   # def MusicaTelaInicial(self):
        #caminho = Path(__file__)
        #pg.mixer.init()
       # menu1 = pg.mixer.Sound('menu1.ogg')
        #somMenu1 = menu1.play()