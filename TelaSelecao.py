import pygame as pg,sys,random

from Configs import *
from Imagens import Imagem
from Jogador import Jogador
from Personagens import Personagem
from Sons import Sons

class TelaSelecao:
    def __init__(self,tela,Fase):
        self.tela = tela
        self.encerra = False
        self.FPS_Clock = pg.time.Clock()
        self.contador = 0
        self.menu = 0
        self.rect = 0
        self.Fase = Fase
        self.count = 0
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.desenha(self.tela)
            self.DefinirJogadores()    

    def tratamento_eventos(self):
        Sons.menu1.play()
        Sons.menu1.set_volume(0.20)
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                sys.exit()
                pg.quit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.encerra = True
                    self.Fase.NumTela = 1
        

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
            tela.blit(Imagem.Hguaraci,(860,310))

            

        self.FPS_Clock.tick(30)
        pg.display.flip()         

    def Selecao(self):
        opcoes = self.SelectMenu(SelecaoPersonagem)
        Player_y = random.randint(292,563)
        Player_x = random.randint(126,1105) 
        if opcoes == 1:
            Personagem = D_Heitor
            NewPlayer = Jogador(posxy=(Player_x,Player_y),personagem=Personagem)
            self.Fase.Jogadores.append(NewPlayer)

        if opcoes == 2:
            Personagem = Ida
            NewPlayer = Jogador(posxy=(Player_x,Player_y),personagem=Personagem)
            self.Fase.Jogadores.append(NewPlayer)

        if opcoes == 3:
            Personagem = Jurupari
            NewPlayer = Jogador(posxy=(Player_x,Player_y),personagem=Personagem)
            self.Fase.Jogadores.append(NewPlayer)
            
        if opcoes == 4:
            Personagem = Guaraci
            NewPlayer = Jogador(posxy=(Player_x,Player_y),personagem=Personagem)
            self.Fase.Jogadores.append(NewPlayer)            

    def DefinirJogadores(self):
        self.count+=1
        if self.count ==1:
            self.Fase.Jogadores.clear()
        if len(self.Fase.Jogadores) == 2:
            self.encerra = True
            self.Fase.NumTela = 3
            Sons.menu1.stop()
        self.Selecao()
        

    def SelectMenu(self,opcoes:list) -> int:
        mx,my = pg.mouse.get_pos()
        for event in pg.event.get():
            if opcoes[0].collidepoint((mx,my)):
                self.rect = 1
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        return 1
            if opcoes[1].collidepoint((mx,my)):
                self.rect = 2
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        return 2
            if opcoes[2].collidepoint((mx,my)):
                self.rect = 3
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        return 3
            if opcoes[3].collidepoint((mx,my)):
                self.rect = 4
                if event.type == pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[0]:
                        return 4
            if (event.type == pg.QUIT):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.encerra = True
                self.Fase.NumTela = 1