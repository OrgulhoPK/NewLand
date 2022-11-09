from pathlib import Path
import pygame as pg


class Imagem:
    caminho = Path(__file__)
    esquerda_direitaP1 = caminho.parent / 'P1' / 'P1-andar' / 'esquerda-direita'
    cimaP1 = caminho.parent / 'P1' / 'P1-andar' / 'cima'
    baixoP1 = caminho.parent / 'P1' / 'P1-andar' / 'baixo'
 
    andarP1D = [] #esquerda | direita
    andarP1C = [] #cima P1
    andarP1B = [] #baixo P1
    for i in esquerda_direitaP1.glob("*.png"):
        andarP1D.append(pg.image.load(i))

    for i in cimaP1.glob("*.png"):
        andarP1C.append(pg.image.load(i))

    for i in baixoP1.glob("*.png"):
        andarP1B.append(pg.image.load(i))


