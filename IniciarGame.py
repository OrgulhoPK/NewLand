import pygame as pg

from Configs import *
import sys,random
from Inimigos import Inimigo
from Imagens import Imagem
#from Sons import Sons


class Game:
    def __init__(self,tela,jogadores):
        #tela e configuracoes locais
        self.FPS_CLOCK = pg.time.Clock()
        self.tela = tela
        self.encerrada = False
        self.background = Imagem.Background
        self.estruturas = Imagem.Estruturas
        self.Totem = [Estrutura]

        #jogadores e inimigos
        self.jogador1 = jogadores[0]
        self.jogador2 = jogadores[1]
        self.jogadores = [self.jogador1,self.jogador2]
        self.ListInimigos = ListInimigos
        self.Inimigos = []

    
        #contador e efeitos de arena
        self.contador = 0
        self.lista = Imagem.ListaColisoes
        self.teleporte= setup.areaEfeito
        self.slow = setup.areaEfeito2

    def rodar (self):
        while not self.encerrada:
            self.tratamento_eventos()
            self.Estado_Colisoes(self.lista,self.tela)
            self.desenha(self.tela)     
               
    def tratamento_eventos(self): 
        self.controleInimigos()     
        self.movimentos()
        self.acoes()

        
        for event in pg.event.get():
            tecla = pg.key.get_pressed()
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
                if event.type == pg.KEYDOWN and tecla[pg.K_q]:
                    if self.jogador1.cooldown1 >= 15:
                        self.jogador1.ataque(self.tela,self.Inimigos,self.Totem)

                if event.type == pg.KEYDOWN and tecla[pg.K_e]:
                    if self.jogador1.cooldown2 >= 60:
                        if self.jogador1.nome == 'Jurupari':
                            self.jogador1.mouse = True
                            self.jogador1.ataque_especial(self.tela,self.Inimigos,self.Totem,self.jogador2)
                        else:
                            self.jogador1.ataque_especial(self.tela,self.Inimigos,self.Totem)

                        
                if event.type == pg.KEYDOWN and tecla[pg.K_u]:
                    if self.jogador2.cooldown1 >= 15:
                        self.jogador2.ataque(self.tela,self.Inimigos,self.Totem)

                if event.type == pg.KEYDOWN and tecla[pg.K_o]:
                    if self.jogador2.cooldown2 >= 60:
                        if self.jogador2.nome == 'Jurupari':
                            self.jogador2.mouse = True
                            self.jogador2.ataque_especial(self.tela,self.Inimigos,self.Totem,self.jogador2)
                        else:
                            self.jogador2.ataque_especial(self.tela,self.Inimigos,self.Totem)       

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

        self.teleporte.Teleporte(tela,self.jogadores,self.Inimigos)
        self.slow.Slow(tela,self.jogadores,self.Inimigos)
        
        #desenho jogadores / inimigos
        self.jogador1.desenhar(tela) 
        self.jogador2.desenhar(tela) 
        for inimigo in self.Inimigos:
            inimigo.desenhar(tela),
        self.Totem[0].desenhar(tela)
        
        
        #ultimo setup
        pg.display.update()
        self.FPS_CLOCK.tick(30)
#controle dos projeteis e area de ameaça dos inimigos
    def acoes(self):
        dados = self.Totem + self.Inimigos
        for projetil in self.jogador1.projeteis:
            if projetil.distancia(self.jogador1):
                self.jogador1.projeteis.clear()
            for inimigo in dados:
                if projetil.colisaoProjetil(inimigo) and inimigo.visible:
                    inimigo.hit()
                    self.jogador1.projeteis.clear()

        for projetil in self.jogador2.projeteis:
            if projetil.distancia(self.jogador2):
                self.jogador2.projeteis.clear()
            for inimigo in dados:
                if projetil.colisaoProjetil(inimigo) and inimigo.visible:
                    inimigo.hit()
                    self.jogador2.projeteis.clear()

        for inimigo in self.Inimigos:
            for jogador in self.jogadores:
                #primeiro analisa se tem alguem na area de ameaça, se tiver, analisa se está vivo
                if inimigo.areaameaca(jogador,80):
                   
                    if jogador.visible:
                        #ataques por segundo 0.42 (1 seg, 30 frames) 70*0.42 = 29.4
                        if inimigo.cooldown1 >=70 and not inimigo.stun and not inimigo.atkEspecial:
                            inimigo.ataque(self.tela,self.jogadores)       
                if inimigo.areaameaca(jogador,200):
                    if jogador.visible:
                        if inimigo.cooldown2 >=250 and not inimigo.stun and not inimigo.atk:
                            inimigo.ataque_especial(self.tela,self.jogadores)
                for projetil in inimigo.projeteis:
                    if projetil.distancia(inimigo):
                        inimigo.projeteis.clear()
                    elif projetil.colisaoProjetil(jogador) and jogador.visible:
                        jogador.hit()
                        jogador.stun = True
                        inimigo.projeteis.clear()

        if self.Totem[0].atk:
            self.Totem[0].dados = self.jogadores
#adiciona inimigos na lista Inimigos, até um certo limite  
    def controleInimigos(self):
        for inimigo in self.Inimigos:
            if not inimigo.visible:
                self.Inimigos.remove(inimigo)
        for i in self.ListInimigos:
            if len(self.Inimigos) <2:
                self.Inimigos.append(i)
                self.ListInimigos.remove(i)
#movimento dos jogadores e inimigos
    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela
        tecla = pg.key.get_pressed()
        
        if not self.jogador1.atk and not self.jogador1.atkEspecial and self.jogador1.acao:

            if tecla[pg.K_a] and (self.jogador1.x > 0) :
                self.jogador1.esquerda()
                self.jogador1.mov_vx = -1

            if tecla[pg.K_d] and (self.jogador1.x + 64 < S_WIDHT) :          
                self.jogador1.direita()
                self.jogador1.mov_vx = 1

            if tecla[pg.K_w] and (self.jogador1.y > 0) : 
                self.jogador1.cima()   
                self.jogador1.mov_vy = -1                
                      
            if tecla[pg.K_s] and (self.jogador1.y + 64 < S_HEIGHT) :
                self.jogador1.baixo()
                self.jogador1.mov_vy = 1
            
            #Movimento jogador 2
        if not self.jogador2.atk and not self.jogador2.atkEspecial and self.jogador2.acao:
            if tecla[pg.K_j] and (self.jogador2.x > 0) :
                self.jogador2.esquerda()
                self.jogador2.mov_vx = -1               

            if tecla[pg.K_l] and (self.jogador2.x + 64 < S_WIDHT) :          
                self.jogador2.direita()
                self.jogador2.mov_vx = 1          

            if tecla[pg.K_i] and (self.jogador2.y > 0) : 
                self.jogador2.cima()   
                self.jogador2.mov_vy = -1
                                              
            if tecla[pg.K_k] and (self.jogador2.y + 64 < S_HEIGHT) :
                self.jogador2.baixo()
                self.jogador2.mov_vy = 1
                

        #trata movimento do inimigo
        for inimigo in self.Inimigos:
            if inimigo.acao and not inimigo.stun and not inimigo.atk and not inimigo.atkEspecial:
                inimigo.movimento(self.jogador1,self.jogador2)
#colisoes e estado de debuff(stun ou slow)
    def Estado_Colisoes(self,lista,tela):

        self.jogador1.colisao(lista)
        self.jogador1.atualizarEstado(tela)

        self.jogador2.colisao(lista)
        self.jogador2.atualizarEstado(tela)

        for inimigo in self.Inimigos:
            inimigo.colisao(lista)
            inimigo.atualizarEstado(tela)
        
        if not self.jogador1.mouse and not self.jogador2.mouse:
            for inimigo in self.Inimigos:
                inimigo.acao = True
            self.jogador1.acao = True
            self.jogador2.acao = True
        else:
            for inimigo in self.Inimigos:
                inimigo.acao = False
            self.jogador1.acao = False
            self.jogador2.acao = False
