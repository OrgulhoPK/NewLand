from pathlib import Path
import pygame as pg


class Imagem:
    caminho = Path(__file__)
    

    #Carregamento Menu Inicial
    
    Inicial = caminho.parent / 'Images' / 'Menu Inicial' / 'Tela Fundo'
    Titulo = caminho.parent / 'Images' / 'Menu Inicial' / 'Titulo'
    MenuInicial = []
    NomeTitulo = []
    for i in Inicial.glob('*.png'):
        MenuInicial.append(pg.image.load(i))

    for i in Titulo.glob('*.png'):
        NomeTitulo.append(pg.image.load(i))


    #Carregamento do Mapa PVP
    Map1 = caminho.parent / 'Images' / 'Mapa PVP' / 'Map'
    Centro1 = caminho.parent / 'Images' / 'Mapa PVP' / 'Centro'
    MapPvP= []
    Centro=[]
    for i in Map1.glob('*.png'):
        MapPvP.append(pg.image.load(i))
    for i in Centro1.glob('*.png'):
        Centro.append(pg.image.load(i))



    #carregamento do andar
    esquerda_direitaP1 = caminho.parent / 'Images'/'P1' / 'P1-andar' / 'esquerda-direita'
    cimaP1 = caminho.parent / 'Images'/ 'P1' / 'P1-andar' / 'cima'
    baixoP1 = caminho.parent / 'Images'/ 'P1' / 'P1-andar' / 'baixo'
    
    #animação de andar do clerigo

    andarP1D = [] #esquerda | direita
    andarP1C = [] #cima P1
    andarP1B = [] #baixo P1
    for i in esquerda_direitaP1.glob("*.png"):
        andarP1D.append(pg.image.load(i))

    for i in cimaP1.glob("*.png"):
        andarP1C.append(pg.image.load(i))

    for i in baixoP1.glob("*.png"):
        andarP1B.append(pg.image.load(i))


    #animacao de atk

    caminho2 = caminho.parent / 'Images'/ 'P1' / 'P1 - ataque'
    atk = []

    for i in caminho2.glob("*.png"):
        atk.append(pg.image.load(i))

    


