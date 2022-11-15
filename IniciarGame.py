import pygame as pg

from Configs import Config
from Jogador import Jogador
from Projeteis import Projetil
import sys
from Inimigos import Inimigos
from Imagens import Imagem
from Sons import Sons


class Game:
    def __init__(self,tela):
        pg.init()
        self.FPS_CLOCK = pg.time.Clock()
        self.tela = tela
        self.jogador = Jogador(posXY=(Config.Player_x,Config.Player_y),posWH = (32,32))
        self.projeteis = []
        self.encerrada = False
        self.Inimigos = Inimigos(posXY=(500,300),posWH = (32,32))
        self.contador = 0
        

    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.atualiza_estado()
            self.desenha()         


    def atualiza_estado(self):
        self.jogador.atualizar_posicao()

    def tratamento_eventos(self):         
        self.movimentos()
        #self.colisoes()
        mouse_x,mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    #self.projeteis.append(Projetil(self.jogador.posXY[0]-self.jogador.scroll[0]+32,self.jogador.posXY[1]-self.jogador.scroll[1]+45,mouse_x,mouse_y))
                    self.projeteis.append(Projetil(self.jogador.X+32,self.jogador.Y+45,mouse_x,mouse_y))
                    #Chamando a função de som do projetil quando o botão do projetil é apertado
                    Sons.BarulhoProjetil(self)

        if pg.key.get_pressed()[pg.K_ESCAPE]:
            sys.exit(0)
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            self.encerrada = True
    
    def desenha(self):
        # mapa

        self.tela.blit(Imagem.MapPvP[0], (0,0)) 

        self.contador +=1
        if self.contador +1 >= 176:
            self.contador = 0
        self.tela.blit(Imagem.Centro[self.contador//5],(593,234))


        #desenho jogadores / inimigos
        self.jogador.desenhar(self.tela) 
        self.Inimigos.desenhar(self.tela)

        #Desenho projeteis
        for projeteis in self.projeteis:
                
                projeteis.desenha(self.tela)
                
                projeteis.atk = True
                
        
        #Alguns Detalhes do mapa
        
        self.tela.blit(Imagem.MapPvP[1], (506,329))
        self.tela.blit(Imagem.MapPvP[2], (506,153))
        


        #ultimo setup
        pg.display.flip()
        self.FPS_CLOCK.tick(30)

    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela
        if not self.jogador.atk:
            if pg.key.get_pressed()[pg.K_a] and (self.jogador.X >0) :
                self.jogador.esquerda()
                self.jogador.mov_esquerda = True

            if pg.key.get_pressed()[pg.K_d] and (self.jogador.X + 64 < Config.S_WIDHT):          
                self.jogador.direita()
                self.jogador.mov_direita = True

            if pg.key.get_pressed()[pg.K_w] and (self.jogador.Y > 0):
                self.jogador.cima()   
                self.jogador.mov_cima = True                 
                      
            if pg.key.get_pressed()[pg.K_s] and (self.jogador.Y + 64 < Config.S_HEIGHT):
                self.jogador.baixo()
                self.jogador.mov_baixo = True

            


    #800x 600y

    def colisoes(self):
        '''if self.jogador.posXY[0] < 0:
            self.jogador.movimento = 0
        if self.jogador.posXY[1] < 0:
            self.jogador.posXY[1]= 0
        if self.jogador.right > Config.S_WIdwDHT:
            self.jogador.right = Config.S_WIDHT
        if self.jogador.top <= 0:
            self.jogador.top = 0
        if self.jogador.bottom >= Config.S_HEIGHT:
            self.jogador.bottom = Config.S_HEIGHT'''

        