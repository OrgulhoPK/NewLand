import pygame as pg
import random

class Config:
    S_HEIGHT = 720
    S_WIDHT = 1280
    Player_y = random.randint(288,433)
    Player_x = random.randint(127,433)
    COR_Tela = (24,164,86) #verde
    COR_PlayerTest = (255,255,255) #branco
    COR_InimigoTest = (0,0,0) #preto
    
    #Configuraçoes do Mapa Background Tiles
    MapW, MapH = 16,16
    

    VelWarrior = 0.2

    #adicionadas no teste
    Tela = 0
    #caixa de selecao do menu 1
    TelaInicial = [pg.Rect(541,391,184,33),
                    pg.Rect(508,441,263,37)]
