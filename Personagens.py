import pygame as pg
import Configs


class Personagens:
    def __init__(self,vida,dano,sprites):
        #vida,dano,skillbasica,skillespecial,estado
        self.vida = vida
        self.dano = dano
        self.sprite = sprites
        self.habilidades = []



