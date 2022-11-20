import pygame as pg


class Personagem:
    def __init__(self,vida,dano,sprites):
        #vida,dano,skillbasica,skillespecial,estado
        self.vida = vida
        self.dano = dano
        self.sprites = sprites  #[Esq_dir,cima,baixo,ataque]
        #self.skills = skills
        self.habilidades = []
        
