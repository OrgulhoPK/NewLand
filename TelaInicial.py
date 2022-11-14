import pygame as pg
import sys

from Configs import Config
from Imagens import Imagem

class PrimeiraTela:
    def __init__(self,tela):
        self.tela = tela
        self.encerra = False
        self.fundo = None
        self.FPS_Clock = pg.time.Clock()
        self.contador = 0
        self.opcoes = Config.TelaInicial
        self.menu = 0
    
    def rodar(self):
        while not self.encerra:
            self.tratamento_eventos()
            self.SelectMenu()
            self.desenha(self.tela)
        

    def tratamento_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit()
                pg.quit()




    def desenha(self,tela):

        self.contador +=1
        if self.contador +1 >= 89:
            self.contador = 0


        tela.blit(Imagem.MenuInicial[0], (0,0)) #TelaFundo
        #Titulo animado
        tela.blit(pg.transform.scale(Imagem.NomeTitulo[self.contador//4], (325,214)),(479,66))
        #Subtitulo e opçoes
        tela.blit(Imagem.MenuInicial[1], (500,263))
        if self.menu == 0:
            tela.blit(Imagem.MenuInicial[2], (490,391))
        
        if self.menu == 2:
            tela.blit(Imagem.MenuInicial[3],(490,350))

        self.FPS_Clock.tick(30)
        pg.display.flip()     

    def StoryMode(self):
        self.menu = 1
        while self.menu == 1:
            print("entrou menu pve")
            self.desenha(self.tela)
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    sys.exit()
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.menu = 0

                if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                    Config.Tela += 1
                    self.encerra = False
    def PvP(self):
        self.menu = 2
        while self.menu == 2:
            self.desenha(self.tela)
            print("entrou menu pvp")
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    sys.exit()
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.menu = 0

    def SelectMenu(self):
        mx,my = pg.mouse.get_pos()
        if self.opcoes[0].collidepoint((mx,my)):
            print("collidiu op1")
            if pg.mouse.get_pressed()[0]:
                self.StoryMode()
        if self.opcoes[1].collidepoint((mx,my)):
            print("colidiu op2")
            if pg.mouse.get_pressed()[0]:
                self.PvP()


                
