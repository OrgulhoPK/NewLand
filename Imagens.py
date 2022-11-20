from pathlib import Path
import pygame as pg
from SpriteAndTiles import *


class Imagem:
    caminho = Path(__file__)
    
    #Carregamento Menu Inicial
    Inicial = caminho.parent / 'Imagens' / 'Menu Inicial' / 'Tela Fundo'
    Titulo = caminho.parent / 'Imagens' / 'Menu Inicial' / 'Titulo'
    telaFundo = Inicial / '1 - TelaFundoMenu.png'
    Adventure = Inicial / '2 - the adventure.png'
    opcoes = Inicial / '3 - opcoes.png'
    #Coloquei separado, porque no linux estava lendo no for em ordem diferente
    telaFundo1 = pg.image.load(telaFundo)
    Adventure = pg.image.load(Adventure)
    opcoes = pg.image.load(opcoes)

    NomeTitulo = []
    for i in Titulo.glob('*.png'):
        NomeTitulo.append(pg.image.load(i))
    
    #Carregamento Selecao personagens + Historias
    FundoSelecao = Inicial / 'Tela Selecao.png'
    FundoSelecao1 = pg.image.load(FundoSelecao)

    

    #Carregamento do Mapa PVP e estruturas
    Map = caminho.parent / 'Imagens' / 'Mapa PVP' / 'Map'
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
            frame = tileFundo.get_tile(i,16,16)
            tilesetFundo.append(frame)
    for i in range(0,115): # 115 tiles
            frame = tilesetsBack.get_tile(i,16,16)
            tilesetEstruturas.append(frame)



    #list com os tiles carregados no mapa
    Background = load_tiles(file,tilesetFundo)
    Estruturas = load_tiles(file2,tilesetEstruturas)
    ListaColisoes = []
    for i in Estruturas:
        x,y = i.rect()
        ListaColisoes.append(pg.Rect(x,y,16,16))

    #portal
    Centro=[]
    for i in Centro1.glob('*.png'):
        Centro.append(pg.image.load(i))






    #Animação dos Personagens em ordem
    Personagens = caminho.parent / 'Imagens' / 'Personagens'

    #Clerigo
    Clerigo = Personagens / 'Clerigo'

    #carregamento do andar
    esquerda_direitaP1 =  Clerigo / 'andar' / 'esquerda-direita'
    cimaP1 =  Clerigo / 'andar' / 'cima'
    baixoP1 = Clerigo / 'andar' / 'baixo'   
    
    C_andarP1D = [] #esquerda | direita
    C_andarP1C = [] #cima P1
    C_andarP1B = [] #baixo P1
    for i in esquerda_direitaP1.glob("*.png"):
        C_andarP1D.append(pg.image.load(i))
    for i in cimaP1.glob("*.png"):
        C_andarP1C.append(pg.image.load(i))
    for i in baixoP1.glob("*.png"):
        C_andarP1B.append(pg.image.load(i))

    #animacao de atk
    C_ataque = Clerigo / 'ataque'
    C_atk = []
    for i in C_ataque.glob("*.png"):
        C_atk.append(pg.image.load(i))
    
    Sprites_Clerigo = [C_andarP1D,C_andarP1C,C_andarP1B,C_atk]
    

    


