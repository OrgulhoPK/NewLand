from pathlib import Path
import pygame as pg
from SpriteAndTiles import *
from Configs import Config

class Imagem:
    caminho = Path(__file__)
    
    #Carregamento Menu Inicial
    Inicial = caminho.parent / 'Images' / 'Menu Inicial' / 'Tela Fundo'
    Titulo = caminho.parent / 'Images' / 'Menu Inicial' / 'Titulo'
    telaFundo = Inicial / '1 - TelaFundoMenu.png'
    Adventure = Inicial / '2 - the adventure.png'
    opcoes = Inicial / '3 - opcoes.png'
    menuPvP = Inicial / '4 - Menu PVP.png'
    telaFundo1 = pg.image.load(telaFundo)
    Adventure = pg.image.load(Adventure)
    opcoes = pg.image.load(opcoes)
    menuPvP = pg.image.load(menuPvP)
    MenuInicial = []
    NomeTitulo = []
    for i in Inicial.glob('*.png'):
        MenuInicial.append(pg.image.load(i))
    for i in Titulo.glob('*.png'):
        NomeTitulo.append(pg.image.load(i))



    #Carregamento do Mapa PVP e estruturas

    Map = caminho.parent / 'Images' / 'Mapa PVP' / 'Map'
    file = Map / 'CSVs' / 'Background.csv'
    file2 = Map / 'CSVs' / 'Estruturas.csv'
    Centro1 = caminho.parent / 'Images' / 'Mapa PVP' / 'Centro'

    #leitura e separação do tileset
    localTile1 = Map /'Background.png'
    localTile2 = Map / 'Estruturas.png'
    tileset1 = pg.image.load(localTile1)
    tileFundo = TileSet(tileset1)
    tilesetFundo = []
    tileset2 = pg.image.load(localTile2)
    tilesetsBack = TileSet(tileset2)
    tilesetEstruturas = []

    for i in range(0,186): # 186 tiles
            frame = tileFundo.get_tile(i,Config.MapW,Config.MapH)
            tilesetFundo.append(frame)
    for i in range(0,115): # 115 tiles
            frame = tilesetsBack.get_tile(i,Config.MapW,Config.MapH)
            tilesetEstruturas.append(frame)



    #list com os tiles carregados no mapa

    Background = load_tiles(file,tilesetFundo)
    Estruturas = load_tiles(file2,tilesetEstruturas)
    ListaColisoes = []
    for i in Estruturas:
        x,y = i.rect()
        ListaColisoes.append(pg.Rect(x,y,16,16))
    rec = pg.Rect(0,0,1,1)
    #union = rec.unionall_ip(ListaColisoes)


    Centro=[]
    for i in Centro1.glob('*.png'):
        Centro.append(pg.image.load(i))




    #carregamento do andar
    MovimentoP1 = caminho.parent / 'Images'/'P1' / 'P1-andar'
    esquerda_direitaP1 =  MovimentoP1 / 'esquerda-direita'
    cimaP1 =  MovimentoP1 / 'cima'
    baixoP1 = MovimentoP1 / 'baixo'
    
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

    


