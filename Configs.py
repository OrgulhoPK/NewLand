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
D_Heitor = Personagem('Heitor',30,4,[5,150],Imagem.Sprites_Clerigo,SkillsHeitor)
Ida = Personagem('Ida',35,5,[20,150],Imagem.Sprites_Duelista,SkillsIda)
Jurupari = Personagem('Jurupari',20,4,[3,450],Imagem.Sprites_Shaman,SkillsJurupari)
Guaraci = Personagem('Guaraci',50,3,[40,200],Imagem.Sprites_Tanker,SkillsGuaraci)



#Lista de habilidades Inimigas 
SkillsBoss = [Skill(5,Imagem.hitDamage),Skill(20,Imagem.StunMob1)]
SkillsSoldado= [Skill(5,Imagem.hitDamage),Skill(20,Imagem.StunMob1)]
SkillsTotem = [Skill(55,Imagem.circuloTotem),None]
#Mob
Boss = Personagem('Boss',300,2,[70,250],Imagem.Sprites_Boss,SkillsBoss)
Soldadinho = Personagem('Soldado',60,2,[70,250],Imagem.Sprites_Soldadinho,SkillsSoldado)
Totem = Personagem('Estrutura',7,0,[0,0],Imagem.Sprites_Totem,SkillsTotem)

#Efeitos
Stun = Imagem.starStun1

#Setup para configurar e editar valores 
Estrutura = (Inimigo(posxy=(234,450),personagem=Totem))
class setup:
    NumTela = 0
    Jogadores = []
    areaEfeito = Skill(5,Imagem.Teleport,682,420)
    areaEfeito2 = Skill(5,Imagem.Slow,682,420)

    ListInimigos = []
    ListBoss = []

    def adicionarInimigos(self):
        if not self.ListBoss and not self.ListInimigos:
            self.ListBoss.append(Inimigo(posxy=(500,300),personagem=Boss))
            for i in range (0,30):
                x = random.randint(525,750)
                y = random.randint(200,370)
                self.ListInimigos.append(Inimigo(posxy=(x,y),personagem=Soldadinho))




