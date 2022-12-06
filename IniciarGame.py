import pygame as pg

from Configs import *
import sys
from Inimigos import Inimigo
from Imagens import Imagem
#from Sons import Sons


class Game:
    def __init__(self,tela,jogadores):

        self.FPS_CLOCK = pg.time.Clock()
        self.tela = tela
        #self.jogador = Jogador(posxy=( Player_x, Player_y),posWH = (32,32),personagem=)
        self.jogador1 = jogadores[0]
        self.jogador2 = jogadores[1]
        self.jogadores = [self.jogador1,self.jogador2]
        self.melee = []
        self.projeteis = []
        self.encerrada = False
        self.ListInimigos= ListInimigos
        self.InimigosInvocados = []
        self.Inimigos = [Inimigo(posxy=(991,350),personagem=Soldadinho),Inimigo(posxy=(950,340),personagem=Soldadinho)]
        self.contador = 0
        self.background = Imagem.Background
        self.estruturas = Imagem.Estruturas
        self.lista = Imagem.ListaColisoes
        self.mov = False

    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.colisoes(self.lista)
            self.desenha(self.tela)     
               


    def tratamento_eventos(self):      
        self.movimentos()
        self.acoes()
        self.controleInimigos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()    
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:        
                self.encerrada = True
                setup.NumTela = 2
                setup.Jogadores.clear()

            #tratamento dos ataques
            #teclas de ataque básico
            if self.jogador1.acao and self.jogador2.acao:
                if event.type == pg.KEYDOWN and event.key == pg.K_q:
                    if self.jogador1.cooldown1 >= 15:
                        self.jogador1.ataque(self.tela,self.Inimigos)

                if event.type == pg.KEYDOWN and event.key == pg.K_e:
                    if self.jogador1.cooldown2 >= 60:
                        if self.jogador1.nome == 'Jurupari':
                            self.jogador1.mouse = True
                            self.jogador1.ataque_especial(self.tela,self.Inimigos,self.jogador2)
                        else:
                            self.jogador1.ataque_especial(self.tela,self.Inimigos)

                        
                if event.type == pg.KEYDOWN and event.key == pg.K_u:
                    if self.jogador2.cooldown1 >= 15:
                        self.jogador2.ataque(self.tela,self.Inimigos)

                if event.type == pg.KEYDOWN and event.key == pg.K_o:
                    if self.jogador2.cooldown2 >= 60:
                        if self.jogador2.nome == 'Jurupari':
                            self.jogador2.mouse = True
                            self.jogador2.ataque_especial(self.tela,self.Inimigos,self.jogador1)
                        else:
                            self.jogador2.ataque_especial(self.tela,self.Inimigos)
                    


        
            
        
            

    def acoes(self):

        for projetil in self.jogador1.projeteis:
            if projetil.distancia(self.jogador1):
                self.jogador1.projeteis.remove(projetil)
            for inimigo in self.Inimigos:
                if projetil.colisaoProjetil(inimigo) and inimigo.visible:
                    inimigo.hit()
                    self.jogador1.projeteis.remove(projetil)

        for projetil in self.jogador2.projeteis:
            if projetil.distancia(self.jogador2):
                self.jogador2.projeteis.remove(projetil)
            for inimigo in self.Inimigos:
                if projetil.colisaoProjetil(self.Inimigo1) and self.Inimigo1.visible:
                    self.Inimigo1.hit()
                    self.jogador2.projeteis.remove(projetil)

        for inimigo in self.Inimigos:
            for jogador in self.jogadores:
                if inimigo.areaameaca(jogador,80):
                    #velocidade de atk 1.25
                    if inimigo.cooldown1 >=42 and not inimigo.stun and not inimigo.atkEspecial:
                        inimigo.ataque(self.tela,self.jogadores)
                if inimigo.areaameaca(jogador,200):
                    if inimigo.cooldown2 >=250 and not inimigo.stun and not inimigo.atk:
                        inimigo.ataque_especial(self.tela,self.jogadores)
                for projetil in inimigo.projeteis:
                    if projetil.distancia(inimigo):
                        inimigo.projeteis.remove(projetil)
                    elif projetil.colisaoProjetil(jogador) and jogador.visible:
                        jogador.hit()
                        jogador.stun = True
                        inimigo.projeteis.remove(projetil)

        
    def controleInimigos(self):
        for inimigo in self.Inimigos:
            if not inimigo.visible:
                self.Inimigos.remove(inimigo)
        for i in self.ListInimigos:
            if len(self.Inimigos) <2:
                self.Inimigos.append(i)
                self.ListInimigos.remove(i)

    
    def desenha(self,tela):
        # mapa

        for i in self.background:
            i.desenha(tela)


        for i in self.estruturas:
           i.desenha(tela)


        self.contador +=1
        if self.contador +1 >= 176:
            self.contador = 0
        pg.draw.rect(tela,(0,254,155),(545,200,180,150),1,2)
        tela.blit(Imagem.Centro[self.contador//5],(593,234))
    
        

        #desenho jogadores / inimigos
        
        self.jogador1.desenhar(tela) 
        self.jogador2.desenhar(tela) 
        for inimigo in self.Inimigos:
            inimigo.desenhar(tela)
        
                
        
        #ultimo setup
        pg.display.update()
        self.FPS_CLOCK.tick(30)

    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela

        
        if not self.jogador1.atk and not self.jogador1.atkEspecial and self.jogador1.acao:

            if pg.key.get_pressed()[pg.K_a] and (self.jogador1.x > 0) :
                self.jogador1.esquerda()
                self.jogador1.mov_vx = -1

            if pg.key.get_pressed()[pg.K_d] and (self.jogador1.x + 64 < S_WIDHT) :          
                self.jogador1.direita()
                self.jogador1.mov_vx = 1

            if pg.key.get_pressed()[pg.K_w] and (self.jogador1.y > 0) : 
                self.jogador1.cima()   
                self.jogador1.mov_vy = -1                
                      
            if pg.key.get_pressed()[pg.K_s] and (self.jogador1.y + 64 < S_HEIGHT) :
                self.jogador1.baixo()
                self.jogador1.mov_vy = 1
            
            #Movimento jogador 2
        if not self.jogador2.atk and not self.jogador2.atkEspecial and self.jogador2.acao:
            if pg.key.get_pressed()[pg.K_j] and (self.jogador2.x > 0) :
                self.jogador2.esquerda()
                self.jogador2.mov_vx = -1               

            if pg.key.get_pressed()[pg.K_l] and (self.jogador2.x + 64 < S_WIDHT) :          
                self.jogador2.direita()
                self.jogador2.mov_vx = 1          

            if pg.key.get_pressed()[pg.K_i] and (self.jogador2.y > 0) : 
                self.jogador2.cima()   
                self.jogador2.mov_vy = -1
                                              
            if pg.key.get_pressed()[pg.K_k] and (self.jogador2.y + 64 < S_HEIGHT) :
                self.jogador2.baixo()
                self.jogador2.mov_vy = 1
                

        #trata movimento do inimigo
        for inimigo in self.Inimigos:
            if inimigo.acao and not inimigo.stun and not inimigo.atk and not inimigo.atkEspecial:
                inimigo.movimento(self.jogador1,self.jogador2)


    def colisoes(self,lista):
        self.jogador1.colisao(lista)
        self.jogador2.colisao(lista)

        for inimigo in self.Inimigos:
            inimigo.colisao(lista)


        
    




    #800x 600y

    


        
        

        