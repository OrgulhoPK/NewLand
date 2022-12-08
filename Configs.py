import pygame as pg
import random
from Personagens import Personagem
from Imagens import Imagem
from Habilidades import Skill
from Inimigos import *


#Configuracoes padroes
S_HEIGHT = 720
S_WIDHT = 1280
tela = pg.display.set_mode((S_WIDHT, S_HEIGHT))
Player_y = random.randint(288,433)
Player_x = random.randint(127,433)

#caixa de selecao do menu 1
TelaInicial = [pg.Rect(530,391,184,33),
                pg.Rect(508,441,263,37)]
#caixas selecao menu selecao
SelecaoPersonagem = [pg.Rect(120,249,157,50),
                pg.Rect(120,315,157,50),
                pg.Rect(120,381,157,50),
                pg.Rect(120,444,157,50)]

#Lista de habilidades Aliadas
SkillsIda = [Skill(5,Imagem.hitDamage),Skill(5,Imagem.hitDamage)]
SkillsHeitor = [Skill(20,Imagem.tornado),Skill(92,Imagem.C_Stun1)]
SkillsJurupari = [Skill(5,Imagem.S_fireball1),Skill(92,Imagem.S_CirculoFogo)]
SkillsGuaraci = [Skill(5,Imagem.hitDamage),Skill(35,Imagem.circuloTotem)]


#Lista de personagens
#Personagem = Personagem (vida,dano, Sprites:list , Skills: list)
D_Heitor = Personagem('Heitor',10,10,Imagem.Sprites_Clerigo,SkillsHeitor)
Ida = Personagem('Ida',10,10,Imagem.Sprites_Duelista,SkillsIda)
Jurupari = Personagem('Jurupari',10,10,Imagem.Sprites_Shaman,SkillsJurupari)
Guaraci = Personagem('Guaraci',10,10,Imagem.Sprites_Tanker,SkillsGuaraci)




#Lista de habilidades Inimigas
SkillsSoldado= [Skill(5,Imagem.hitDamage),Skill(20,Imagem.StunMob1)]

#Mob
Soldadinho = Personagem('Soldado',100,10,Imagem.Sprites_Soldadinho,SkillsSoldado)

#Efeitos
Stun = Imagem.starStun1

#Setup para configurar e editar valores 
class setup:
    NumTela = 0
    Jogadores = []
    areaEfeito = Skill(5,Imagem.Teleport,682,420)
    areaEfeito2 = Skill(5,Imagem.Slow,682,420)



ListInimigos = []

for i in range (0,30):
    x = random.randint(525,750)
    y = random.randint(200,370)
    ListInimigos.append(Inimigo(posxy=(x,y),personagem=Soldadinho))




