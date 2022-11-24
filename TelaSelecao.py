import pygame as pg,sys,random

from Configs import *
from Imagens import Imagem
from Jogador import Jogador
from Personagens import Personagem

class TelaSelecao:
    def __init__(self,tela):
        self.tela = tela
        self.encerra = False
        self.FPS_Clock = pg.time.Clock()
        self.contador = 0
        self.opcoes = 0
        self.menu = 0
        self.rect = 0
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha(self.tela)
            self.Selecao(self.tela)    

    def tratamento_eventos(self):
    
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                sys.exit()
                pg.quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.encerra = True
                Telas = 1



    def desenha(self,tela):
        self.contador += 1
        if self.contador +1 >= 56:
            self.contador = 0
        corArcoIris = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tela.blit(Imagem.FundoSelecao1, (0,0))
        tela.blit(Imagem.NomeTitulo[self.contador//4],(540,0))



        if self.rect == 1:
            pg.draw.rect(tela,corArcoIris,SelecaoPersonagem[0],2)
            tela.blit(pg.transform.scale(Imagem.C_andarD[self.contador//8], (64,64)),(310,235))
            tela.blit(Imagem.HHeitor,(860,310))



        if self.rect == 2:
            pg.draw.rect(tela,corArcoIris,SelecaoPersonagem[1],2)
            tela.blit(pg.transform.scale(Imagem.D_andarD[self.contador//8], (64,64)),(310,300))
            tela.blit(Imagem.HIda,(860,310))

        if self.rect == 3:
            pg.draw.rect(tela,corArcoIris,SelecaoPersonagem[2],2)
            tela.blit(pg.transform.scale(Imagem.S_andarD[self.contador//8], (64,64)),(310,365))
            tela.blit(Imagem.HJurupari,(860,310))

        if self.rect == 4:
            pg.draw.rect(tela,corArcoIris,SelecaoPersonagem[3],2)
            tela.blit(pg.transform.scale(Imagem.T_andarD[self.contador//8], (64,64)),(310,430))

            

        self.FPS_Clock.tick(30)
        pg.display.flip()
        
            
    
                

    def Selecao(self,tela):
        self.opcoes = self.SelectMenu(SelecaoPersonagem)

        if self.opcoes == 1:
            Personagem = D_Heitor
            NewPlayer = Jogador(posXY=(Player_x,Player_y),posWH = (32,32),personagem=Personagem)
            AdicionarJogador(NewPlayer)
            self.encerra = True
            setup.NumTela = 3
        if self.opcoes == 2:
            Personagem = Ida
            NewPlayer = Jogador(posXY=(Player_x,Player_y),posWH = (32,32),personagem=Personagem)
            AdicionarJogador(NewPlayer)
            self.encerra = True
            setup.NumTela = 3
        if self.opcoes == 3:
            Personagem = Jurupari
            NewPlayer = Jogador(posXY=(Player_x,Player_y),posWH = (32,32),personagem=Personagem)
            AdicionarJogador(NewPlayer)
            self.encerra = True
            setup.NumTela = 3
        if self.opcoes == 4:
            Personagem = Ubiratan
            NewPlayer = Jogador(posXY=(Player_x,Player_y),posWH = (32,32),personagem=Personagem)
            AdicionarJogador(NewPlayer)
            self.encerra = True
            setup.NumTela = 3


    def SelectMenu(self,opcoes):
        mx,my = pg.mouse.get_pos()
        if opcoes[0].collidepoint((mx,my)):
            self.rect = 1
            if pg.mouse.get_pressed()[0]:
                return 1
        if opcoes[1].collidepoint((mx,my)):
            self.rect = 2
            if pg.mouse.get_pressed()[0]:
                return 2
        if opcoes[2].collidepoint((mx,my)):
            self.rect = 3
            if pg.mouse.get_pressed()[0]:
                return 3
        if opcoes[3].collidepoint((mx,my)):
            self.rect = 4
            if pg.mouse.get_pressed()[0]:
                return 4
    