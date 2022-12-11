from pathlib import Path
import pygame as pg


class Sons:
    pass
    caminho = Path(__file__)
    pg.mixer.init()


   #Chamando as musicas
    menu1 = pg.mixer.Sound('Sons/menu1.wav')

    batalha = pg.mixer.Sound('Sons/overworld.wav')

    ataque = pg.mixer.Sound('Sons/whoosh.wav')


    
    
    
    
   