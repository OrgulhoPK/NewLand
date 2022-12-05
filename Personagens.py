import pygame as pg
from Habilidades import Skill

class Personagem:
    def __init__(self,nome,vida,dano,sprites,habilidade:Skill):
        #vida,dano,skillbasica,skillespecial,estado
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.sprites = sprites  #[Esq_dir,cima,baixo,ataque]
        #self.skills = skills
        self.habilidade = habilidade

    def sleep(self):
        pass
        
