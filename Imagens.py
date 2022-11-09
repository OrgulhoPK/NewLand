from pathlib import Path
import pygame as pg


class Imagem:
    caminho = Path(__file__)
    imagens = caminho.parent / 'andar' 
    andar = []
    
    for i in imagens.glob("*.png"):
        andar.append(pg.image.load(i))


