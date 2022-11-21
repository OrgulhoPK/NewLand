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
    Centro1 = caminho.parent / 'Imagens' / 'Mapa PVP' / 'Centro'

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
    
    C_andarD = [] #esquerda | direita
    C_andarC = [] #cima P1
    C_andarB = [] #baixo P1
    for i in esquerda_direitaP1.glob("*.png"):
        C_andarD.append(pg.image.load(i))
    for i in cimaP1.glob("*.png"):
        C_andarC.append(pg.image.load(i))
    for i in baixoP1.glob("*.png"):
        C_andarB.append(pg.image.load(i))

    #animacao de atk
    C_ataque = Clerigo / 'ataque' / 'esquerda-direita'
    # [cima,baixo,esquerda-direita]
    C_atk = []
    for i in C_ataque.glob("*.png"):
        C_atk.append(pg.image.load(i))
    
    Sprites_Clerigo = [C_andarD,C_andarC,C_andarB,C_atk]


    #Duelista
    Duelista = Personagens / 'Duelista'

    #carregamento do andar
    esquerda_direitaP2 =  Duelista / 'andar' / 'esquerda-direita'
    cimaP2 =  Duelista / 'andar' / 'cima'
    baixoP2 = Duelista / 'andar' / 'baixo'   
    
    D_andarD = [] #esquerda | direita
    D_andarC = [] #cima P1
    D_andarB = [] #baixo P1
    for i in esquerda_direitaP2.glob("*.png"):
        D_andarD.append(pg.image.load(i))
    for i in cimaP2.glob("*.png"):
        D_andarC.append(pg.image.load(i))
    for i in baixoP2.glob("*.png"):
        D_andarB.append(pg.image.load(i))

    #animacao de atk
    D_ataque = Duelista / 'ataque' / 'esquerda-direita'
    D_atk = []
    for i in D_ataque.glob("*.png"):
        D_atk.append(pg.image.load(i))
    
    Sprites_Duelista = [D_andarD,D_andarC,D_andarB,D_atk]


    #Shaman
    Shaman = Personagens / 'Shaman'

    #carregamento do andar
    esquerda_direitaP3 =  Shaman / 'andar' / 'esquerda-direita'
    cimaP3 =  Shaman / 'andar' / 'cima'
    baixoP3 = Shaman / 'andar' / 'baixo'   
    
    S_andarD = [] #esquerda | direita
    S_andarC = [] #cima P3
    S_andarB = [] #baixo P3
    for i in esquerda_direitaP3.glob("*.png"):
        S_andarD.append(pg.image.load(i))
    for i in cimaP3.glob("*.png"):
        S_andarC.append(pg.image.load(i))
    for i in baixoP3.glob("*.png"):
        S_andarB.append(pg.image.load(i))

    #animacao de atk
    S_ataque = Shaman / 'ataque' / 'esquerda-direita'
    S_atk = []
    for i in S_ataque.glob("*.png"):
        S_atk.append(pg.image.load(i))
    
    Sprites_Shaman = [S_andarD,S_andarC,S_andarB,S_atk]
    

    


