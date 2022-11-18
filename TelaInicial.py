import pygame as pg
import sys

from Configs import Config
from Imagens import Imagem
from Sons import Sons

class PrimeiraTela:
    
    def __init__(self,tela):
        self.tela = tela
        self.encerra = False
        self.FPS_Clock = pg.time.Clock()
        self.contador = 0
        self.opcoes = 0
        self.menu = 0
    
    def rodar(self):
        while not self.encerra:
            #Chamando o volume da musica do menu
            Sons.menu1.play()
            #Mudando o volume da musica do menu iniciar
            Sons.menu1.set_volume(0.01)
            self.tratamento_eventos()
            self.desenha(self.tela)

    
    
    
        
        
         

    
    def tratamento_eventos(self):
        for event in pg.event.get():
            if (event.type == pg.QUIT) or \
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                sys.exit()
                pg.quit()

        self.opcoes = self.SelectMenu(Config.TelaInicial)

        if self.opcoes == 1:
            self.StoryMode()
        
        if self.opcoes == 2:
            self.PvP()





    def desenha(self,tela):

        self.contador +=1
        if self.contador +1 >= 89:
            self.contador = 0

        tela.blit(Imagem.telaFundo1, (0,0))
        #Titulo animado
        tela.blit(pg.transform.scale(Imagem.NomeTitulo[self.contador//4], (325,214)),(479,66))
        #Subtitulo e opçoes

        tela.blit(Imagem.Adventure, (500,263))
        if self.menu == 0:
            tela.blit(Imagem.opcoes, (490,391))
        
        if self.menu == 2:
            tela.blit(Imagem.menuPvP,(490,350))

        self.FPS_Clock.tick(30)
        pg.display.flip()     


    def StoryMode(self):
        self.menu = 1
        while self.menu == 1:
            self.desenha(self.tela)
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    sys.exit()
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.menu = 0


    def PvP(self): 
        TelaInicial = [pg.Rect(560,424,130,29),
                        pg.Rect(560,480,151,29)]
        self.menu = 2
        
        while self.menu == 2:
            self.opcoes = self.SelectMenu(TelaInicial)
            self.desenha(self.tela)
            for event in pg.event.get():
                if (event.type == pg.QUIT):
                    sys.exit()
                    pg.quit()
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.menu = 0
            if self.opcoes == 1:
                self.menu = 0
                Sons.menu1.stop()
                self.encerra = True
                Config.Tela = 2
            if self.opcoes == 2:
                if pg.mouse.get_pressed()[0]:
                    self.menu = 0
            


    def SelectMenu(self,opcoes):
        mx,my = pg.mouse.get_pos()
        if opcoes[0].collidepoint((mx,my)):
            if pg.mouse.get_pressed()[0]:
                return 1
        if opcoes[1].collidepoint((mx,my)):
            if pg.mouse.get_pressed()[0]:
                return 2

        

        
                
