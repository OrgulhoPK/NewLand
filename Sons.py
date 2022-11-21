from pathlib import Path
import pygame as pg


class Sons:
    pass
    caminho = Path(__file__)
    pg.mixer.init()


    #Chamando a musica menu
    #som = caminho.parent / 'menu1.ogg'
    menu1 = pg.mixer.Sound('menu1.wav')

    
    
    
    
    
    def BarulhoProjetil(self):
        caminho = Path(__file__)
        pg.mixer.init()
        barulho = pg.mixer.Sound('whoosh.wav')
        som = barulho.play()


    def MusicaTelaInicial(self):
        
        pg.mixer.init()
        menu1 = pg.mixer.Sound('menu1.wav')
        somMenu1 = menu1.play()