import pygame as pg
import random

class Config:
    S_HEIGHT = 720
    S_WIDHT = 1280
    Player_y = random.randint(0,S_HEIGHT - 80)
    Player_x = random.randint(0,S_WIDHT - 80)
    COR_Tela = (24,164,86) #verde
    COR_PlayerTest = (255,255,255) #branco
    COR_InimigoTest = (0,0,0) #preto

    VelWarrior = 0.2

    #adicionadas no teste
    Tela = 0
    #caixa de selecao do menu 1
    TelaInicial = [pg.Rect(541,391,184,33),
                    pg.Rect(508,441,263,37)]
