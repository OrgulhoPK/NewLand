import pygame as pg
import random
from Personagens import Personagem
from Imagens import Imagem



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


#Lista de personagens
#Personagem = Personagem (vida,dano,Sprites:list , Skills: list)
D_Heitor = Personagem(10,10,Imagem.Sprites_Clerigo)
Ida = Personagem(10,10,Imagem.Sprites_Duelista)
Jurupari = Personagem(10,10,Imagem.Sprites_Shaman)

#Mob
Soldadinho = Personagem(10,10,Imagem.Sprites_Soldadinho)



#Jogadores 1 e 2
Jogadores = []
def AdicionarJogador(NewPlayer):
    Jogadores.append(NewPlayer)


class setup:
    NumTela = 0



