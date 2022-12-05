import pygame as pg
import random
from Personagens import Personagem
from Imagens import Imagem
from Habilidades import Skill



S_HEIGHT = 720
S_WIDHT = 1280

tela = pg.display.set_mode((S_WIDHT, S_HEIGHT))
Player_y = random.randint(288,433)
Player_x = random.randint(127,433)
COR_Tela = (24,164,86) #verde
COR_PlayerTest = (255,255,255) #branco
COR_InimigoTest = (0,0,0) #preto


VelWarrior = 0.2
    
#caixa de selecao do menu 1
TelaInicial = [pg.Rect(530,391,184,33),
                pg.Rect(508,441,263,37)]

SelecaoPersonagem = [pg.Rect(120,249,157,50),
                pg.Rect(120,315,157,50),
                pg.Rect(120,381,157,50),
                pg.Rect(120,444,157,50)]




#Lista de habilidades
BasicaIda = Skill(5,Imagem.hitDamage)
BasicaHeitor = [Skill(20,Imagem.tornado),Skill(92,Imagem.C_Stun1)]
SkillsJurupari = [Skill(5,Imagem.S_fireball1),Skill(92,Imagem.S_CirculoFogo)]


#Lista de personagens
#Personagem = Personagem (vida,dano,Sprites:list , Skills: list)
D_Heitor = Personagem('Heitor',10,10,Imagem.Sprites_Clerigo,BasicaHeitor)
Ida = Personagem('Ida',10,10,Imagem.Sprites_Duelista,BasicaIda)
Jurupari = Personagem('Jurupari',10,10,Imagem.Sprites_Shaman,SkillsJurupari)
Guaraci = Personagem('Guaraci',10,10,Imagem.Sprites_Tanker,BasicaIda)


#Mob
Soldadinho = Personagem('Soldadinho',300,10,Imagem.Sprites_Soldadinho,BasicaIda)


#Efeitos
Stun = Imagem.starStun1
#Jogadores 1 e 2

class setup:
    NumTela = 0
    Jogadores = []






