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
    historiaJogo = Inicial / '4 - TelaHistoria.png'
    #Coloquei separado, porque no linux estava lendo no for em ordem diferente
    telaFundo1 = pg.image.load(telaFundo)
    Adventure = pg.image.load(Adventure)
    opcoes = pg.image.load(opcoes)
    historia = pg.image.load(historiaJogo)
    NomeTitulo = []
    for i in Titulo.glob('*.png'):
        NomeTitulo.append(pg.image.load(i))
    

    #Carregamento Selecao personagens + Historias

    FundoSelecao = Inicial / 'Tela Selecao.png'
    FundoSelecao1 = pg.image.load(FundoSelecao)
    Historia_Heitor = Inicial / 'Historia_D.Heitor.png'
    HHeitor = pg.image.load(Historia_Heitor)
    Historia_Ida = Inicial / 'Historia_Ida.png'
    HIda = pg.image.load(Historia_Ida)
    Historia_Jurupari = Inicial / 'Historia_Jurupari.png'
    HJurupari = pg.image.load(Historia_Jurupari)
    Historia_Guaraci = Inicial / 'Historia_Guaraci.png'
    Hguaraci = pg.image.load(Historia_Guaraci)

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





    #TODAS ANIMACOES DE PERSONAGEM (INCLUINDO HABILIDADES E MAPA EFEITOS)
    
    #Animação dos Personagens em ordem
    Personagens = caminho.parent / 'Imagens' / 'Personagens'

    #Clerigo ---------------------------------
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
    C_atk = []
    for i in C_ataque.glob("*.png"):
        C_atk.append(pg.image.load(i))

    C_special = Clerigo / 'ataque' / 'Especial'    
    C_spec = []
    for i in C_special.glob("*.png"):
        C_spec.append(pg.image.load(i))
    
    Sprites_Clerigo = [C_andarD,C_andarC,C_andarB,C_atk,C_spec]
  
    #Duelista ------------------------
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
    #animacao de especial
    D_special = Duelista / 'ataque' / 'Especial'
    D_spec = []
    for i in D_special.glob("*.png"):
        D_spec.append(pg.image.load(i))
    
    Sprites_Duelista = [D_andarD,D_andarC,D_andarB,D_atk,D_spec]


    #Shaman -------------------------------
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

    #Animacao de conjuracao shaman
    S_especial = Shaman / 'ataque' / 'Especial'
    S_esp = []
    for i in S_especial.glob("*.png"):
        S_esp.append(pg.image.load(i))

    Sprites_Shaman = [S_andarD,S_andarC,S_andarB,S_atk,S_esp]

    #Tanker -------------------------------
    Tanker = Personagens / 'Tanker'

    #carregamento do andar
    esquerda_direitaP4 =  Tanker / 'andar' / 'esquerda-direita'
    cimaP4 =  Tanker / 'andar' / 'cima'
    baixoP4 = Tanker / 'andar' / 'baixo'   
    
    T_andarD = [] #esquerda | direita
    T_andarC = [] #cima P4
    T_andarB = [] #baixo P4
    for i in esquerda_direitaP4.glob("*.png"):
        T_andarD.append(pg.image.load(i))
    for i in cimaP4.glob("*.png"):
        T_andarC.append(pg.image.load(i))
    for i in baixoP4.glob("*.png"):
        T_andarB.append(pg.image.load(i))

    #animacao de atk
    T_ataque = Tanker / 'ataque' / 'esquerda-direita'
    T_atk = []
    for i in T_ataque.glob("*.png"):
        T_atk.append(pg.image.load(i))
    T_spec = Tanker / 'ataque' / 'esquerda-direita'
    T_spec1 = []
    for i in T_spec.glob("*.png"):
        T_spec1.append(pg.image.load(i))

    Sprites_Tanker = [T_andarD,T_andarC,T_andarB,T_atk,T_spec1]

    #MOB -------------------------------------------

    #Animacao do Mob
    Soldado = Personagens / 'Mob_Soldadinho'

    #carregamento do andar
    esquerda_direitaMob =  Soldado / 'andar' / 'esquerda-direita'
    cimaMob =  Soldado / 'andar' / 'cima'
    baixoMob = Soldado / 'andar' / 'baixo'   
    
    Mob_andarD = [] #esquerda | direita
    Mob_andarC = [] #cima P3
    Mob_andarB = [] #baixo P3
    for i in esquerda_direitaMob.glob("*.png"):
        Mob_andarD.append(pg.image.load(i))
    for i in cimaMob.glob("*.png"):
        Mob_andarC.append(pg.image.load(i))
    for i in baixoMob.glob("*.png"):
        Mob_andarB.append(pg.image.load(i))

    #animacao de atk
    Mob_ataque = Soldado / 'ataque' / 'esquerda-direita'
    Mob_atk = []
    for i in Mob_ataque.glob("*.png"):
        Mob_atk.append(pg.image.load(i))
    
    Mob_Especial = Soldado / 'ataque' / 'Especial'
    Mob_spec = []
    for i in Mob_Especial.glob("*.png"):
        Mob_spec.append(pg.image.load(i))
    
    Sprites_Soldadinho = [Mob_andarD,Mob_andarC,Mob_andarB,Mob_atk,Mob_spec]

    #Animaçoes das habilidades em geral
    #Animação de ataques 
    Habilidades = caminho.parent / 'Imagens' / 'Habilidades'
    
    #Clerigo
    C_tornado = Habilidades / 'tornado'
    tornado = []
    for i in C_tornado.glob("*.png"):
        tornado.append(pg.image.load(i))
    C_Stun = Habilidades / 'RaioStun'
    C_Stun1 = []
    for i in C_Stun.glob("*.png"):
        C_Stun1.append(pg.image.load(i))

    #Shaman
    S_fireball = Habilidades / 'Fireball'
    S_fireball1 = [] 
    for i in S_fireball.glob("*.png"):
        S_fireball1.append(pg.image.load(i))
    
    S_Circulo = Habilidades / 'CirculoFogo'
    S_CirculoFogo = []
    for i in S_Circulo.glob("*.png"):
        S_CirculoFogo.append(pg.image.load(i))

    #outras animaçoes
    circuloT = Habilidades / 'CirculoTotem' / 'circulo magico.png'
    circuloTotem = pg.image.load(circuloT)
    dano = Habilidades / 'hitDamage'
    hitDamage = []
    for i in dano.glob("*.png"):
        hitDamage.append(pg.image.load(i))
    
    starStun = Habilidades / 'StarStun'
    starStun1 = []
    for i in starStun.glob("*.png"):
        starStun1.append(pg.image.load(i))
    
    StunMob = Habilidades / 'StunMob'
    StunMob1 = []
    for i in StunMob.glob("*.png"):
        StunMob1.append(pg.image.load(i))

    #Efeito no chao
    CirculoTeleport = Habilidades / 'Teleporte'
    Teleport = []
    for i in CirculoTeleport.glob("*.png"):
        Teleport.append(pg.image.load(i))

    CirculoSlow = Habilidades / 'Slow'
    Slow = []
    for i in CirculoSlow.glob("*.png"):
        Slow.append(pg.image.load(i))

    
    


