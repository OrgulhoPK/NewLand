import pygame as pg

from Configs import *
import sys,random
from Inimigos import Inimigo
from Imagens import Imagem
from Sons import Sons


class Game:
    def __init__(self,tela,Fase):
        #tela e configuracoes locais
        self.FPS_CLOCK = pg.time.Clock()
        self.font = pg.font.Font('Fonts/runescape_uf.ttf',52)
        self.tela = tela
        self.encerrada = False
        self.background = Imagem.Background
        self.estruturas = Imagem.Estruturas
        self.Finais = Imagem.ListFinais
        self.Totem = [Estrutura]

        #jogadores e inimigos
        self.jogadores = Fase.Jogadores
        self.Inimigos = []
        self.ListInimigos = Fase.ListInimigos
        self.Boss = Fase.ListBoss
        self.Fase = Fase
        #contador e efeitos de arena
        self.contador = 0
        self.ticks = 0
        self.tempo = [5,0]
        self.timepause = False
        self.lista = Imagem.ListaColisoes
        self.teleporte= self.Fase.areaEfeito
        self.slow = self.Fase.areaEfeito2


    def rodar (self):
        while not self.encerrada:
            self.timer()
            self.controleInimigos()
            self.acoes()
            self.movimentos()
            self.Estado_Colisoes(self.lista)   
            self.tratamento_eventos()
            self.desenha(self.tela)  
            self.FimDeJogo(self.tela)
               
    def tratamento_eventos(self):
        Sons.batalha.play()
        Sons.batalha.set_volume(0.30)
        for event in pg.event.get():
            tecla = pg.key.get_pressed()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()    
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:        
                self.encerrada = True
                self.ticks = 0
                self.Fase.NumTela = 2
                self.Fase.Jogadores.clear()
                Sons.batalha.stop()
            #tratamento dos ataques
            #teclas de ataque básico e especial
            # a condição de time das skills (cololdown >= Tempo de resfriamento da skill)
            if self.jogadores[0].acao and self.jogadores[1].acao:
                if event.type == pg.KEYDOWN and tecla[pg.K_q]:
                    if self.jogadores[0].cooldown1 >= self.jogadores[0].timeSkills[0] and not self.jogadores[0].stun:
                        self.jogadores[0].ataque(self.tela,self.Inimigos,self.Totem)

                if event.type == pg.KEYDOWN and tecla[pg.K_e]:
                    if self.jogadores[0].cooldown2 >= self.jogadores[0].timeSkills[1] and not self.jogadores[0].stun:
                        if self.jogadores[0].nome == 'Jurupari':
                            self.jogadores[0].mouse = True
                            self.jogadores[0].ataque_especial(self.tela,self.Inimigos,self.Totem,self.jogadores[1])
                        else:
                            self.jogadores[0].ataque_especial(self.tela,self.Inimigos,self.Totem)
        
                if event.type == pg.KEYDOWN and tecla[pg.K_u]:
                    if self.jogadores[1].cooldown1 >=  self.jogadores[1].timeSkills[0] and not self.jogadores[1].stun:
                        self.jogadores[1].ataque(self.tela,self.Inimigos,self.Totem)

                if event.type == pg.KEYDOWN and tecla[pg.K_o]:
                    if self.jogadores[1].cooldown2 >=  self.jogadores[0].timeSkills[1] and not self.jogadores[1].stun:
                        if self.jogadores[1].nome == 'Jurupari':
                            self.jogadores[1].mouse = True
                            self.jogadores[1].ataque_especial(self.tela,self.Inimigos,self.Totem,self.jogadores[1])
                        else:
                            self.jogadores[1].ataque_especial(self.tela,self.Inimigos,self.Totem)       

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
        self.jogadores[0].desenhar(tela) 
        self.jogadores[1].desenhar(tela) 
        for inimigo in self.Inimigos:
            inimigo.desenhar(tela),
        self.Totem[0].desenhar(tela)

        text = self.font.render((f'{self.tempo[0]:02}:{self.tempo[1]:02}'), 1, (0,0,0))
        tela.blit(text,(580,2))

        #Desenhos da tela Vitoria / Derrota
        if not(self.ListInimigos) and not(self.Inimigos) and not(self.Boss):
            tela.blit(pg.transform.scale(self.Finais[0],(1280,720)),(0,0))
        if not(self.jogadores[0].visible) and not(self.jogadores[1].visible):
            tela.blit(pg.transform.scale(self.Finais[1],(1280,720)),(0,0))
        if self.tempo[0]==0 and self.tempo[1]==0:
            tela.blit(pg.transform.scale(self.Finais[2],(1280,720)),(0,0))

        #ultimo setup
        pg.display.update()
        self.FPS_CLOCK.tick(30)
    
#relogio de timer do jogo tempo [min , seg]
    def timer(self):
        if not self.timepause:
            if self.tempo[1]<0:
                self.tempo[0]-=1
                self.tempo[1]=59
            if self.ticks%30 == 0:
                self.tempo[1]-=1
            self.ticks += 1
#controle dos projeteis e area de ameaça dos inimigos
#Tem um try / except na função para se o projetil acertar 2 inimigos (chamava a função de remover 2x)
    def acoes(self):
        dados = self.Totem + self.Inimigos
        for projetil in self.jogadores[0].projeteis:
            if projetil.distancia(self.jogadores[0]):
                self.jogadores[0].projeteis.remove(projetil)

                    
            for inimigo in dados:
                if projetil.colisaoProjetil(inimigo) and inimigo.visible:
                    inimigo.hit(10)
                    try:
                        self.jogadores[0].projeteis.remove(projetil)
                    except ValueError:
                        pass
        for projetil in self.jogadores[1].projeteis:
            if projetil.distancia(self.jogadores[1]):
                    self.jogadores[1].projeteis.remove(projetil)
            for inimigo in dados:
                if projetil.colisaoProjetil(inimigo) and inimigo.visible:
                    inimigo.hit(10)
                    try:
                        self.jogadores[1].projeteis.remove(projetil)
                    except ValueError:
                        pass
                        
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
                        jogador.hit(3)
                        jogador.stun = True
                        try:
                            inimigo.projeteis.remove(projetil)
                        except ValueError:
                            pass
        if self.Totem[0].atk:
            self.Totem[0].dados = self.jogadores
#adiciona inimigos na lista Inimigos, até um certo limite  
    def controleInimigos(self):
        #Remove o inimigo ao morrer
        for inimigo in self.Inimigos:
            if not inimigo.visible:
                self.Inimigos.remove(inimigo)
            if inimigo.summons:
                try:
                    self.Inimigos.append(inimigo.summons[0])
                    inimigo.summons.clear()
                except ValueError:
                    pass
                
        #adiciona um inimigo de tempo em tempo e remove da lista de inimigos
        for i in self.ListInimigos:
            if self.tempo[1]%18 == 0 and len(self.Inimigos)<3 and self.ListInimigos:
                self.Inimigos.append(i)
                self.ListInimigos.remove(i)
        #adiciona se nao tiver nenhum inimigo na arena
            if not self.Inimigos:
                self.Inimigos.append(i)
                self.ListInimigos.remove(i)
            
        #Invoca o boss quando nao tiver mais nenhum inimigo na lista 
        if not self.ListInimigos and self.Boss:
            for i in self.Boss:
                self.Inimigos.append(i)
                self.Boss.remove(i)
        #Referente à habilidade especial do boss


#movimento dos jogadores e inimigos
    def movimentos(self):
        #trata somente dos movimentos dos jogadores
        # E trata dos limites de tela
        tecla = pg.key.get_pressed()
        if not self.jogadores[0].atk and not self.jogadores[0].atkEspecial and self.jogadores[0].acao and not self.jogadores[0].stun:
            if tecla[pg.K_a] and (self.jogadores[0].x > 0) :
                self.jogadores[0].esquerda()
                self.jogadores[0].mov_vx = -1

            if tecla[pg.K_d] and (self.jogadores[0].x + 64 < S_WIDHT) :          
                self.jogadores[0].direita()
                self.jogadores[0].mov_vx = 1

            if tecla[pg.K_w] and (self.jogadores[0].y > 0) : 
                self.jogadores[0].cima()   
                self.jogadores[0].mov_vy = -1                
                      
            if tecla[pg.K_s] and (self.jogadores[0].y + 64 < S_HEIGHT) :
                self.jogadores[0].baixo()
                self.jogadores[0].mov_vy = 1
                
            
            #Movimento jogador 2
        if not self.jogadores[1].atk and not self.jogadores[1].atkEspecial and self.jogadores[1].acao and not self.jogadores[1].stun:
            if tecla[pg.K_j] and (self.jogadores[1].x > 0) :
                self.jogadores[1].esquerda()
                self.jogadores[1].mov_vx = -1               

            if tecla[pg.K_l] and (self.jogadores[1].x + 64 < S_WIDHT) :          
                self.jogadores[1].direita()
                self.jogadores[1].mov_vx = 1          

            if tecla[pg.K_i] and (self.jogadores[1].y > 0) : 
                self.jogadores[1].cima()   
                self.jogadores[1].mov_vy = -1
                                              
            if tecla[pg.K_k] and (self.jogadores[1].y + 64 < S_HEIGHT) :
                self.jogadores[1].baixo()
                self.jogadores[1].mov_vy = 1
                

        #trata movimento do inimigo
        for inimigo in self.Inimigos:
            if inimigo.acao and not inimigo.stun and not inimigo.atk and not inimigo.atkEspecial:
                inimigo.movimento(self.jogadores[0],self.jogadores[1])
#colisoes e estado de debuff(stun ou slow)
    def FimDeJogo(self,tela):
        if not(self.jogadores[0].visible) and not(self.jogadores[1].visible):
            self.timepause = True
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()    
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:        
                    self.encerrada = True
                    self.ticks = 0
                    self.Fase.NumTela = 1
                    self.Fase.Jogadores.clear()
                    Sons.batalha.stop()
                    self.timepause = False
        if self.tempo[0]==0 and self.tempo[1]==0:
            self.tempo = [0,0]
            self.timepause = True
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()    
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:        
                    self.encerrada = True
                    self.ticks = 0
                    self.Fase.NumTela = 1
                    self.Fase.Jogadores.clear()
                    Sons.batalha.stop()
                    self.timepause = False
        if not(self.ListInimigos) and not(self.Inimigos) and not(self.Boss):
            self.timepause = True
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()    
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:        
                    self.encerrada = True
                    self.ticks = 0
                    self.Fase.NumTela = 1
                    self.Fase.Jogadores.clear()
                    Sons.batalha.stop()
                    self.timepause = False
        
        




    def Estado_Colisoes(self,lista):

        self.jogadores[0].colisao(lista)
        self.jogadores[0].atualizarEstado()

        self.jogadores[1].colisao(lista)
        self.jogadores[1].atualizarEstado()

        for inimigo in self.Inimigos:
            inimigo.colisao(lista)
            inimigo.atualizarEstado()
        
        if not self.jogadores[0].mouse and not self.jogadores[1].mouse:
            for inimigo in self.Inimigos:
                inimigo.acao = True
            self.jogadores[0].acao = True
            self.jogadores[1].acao = True
        else:
            for inimigo in self.Inimigos:
                inimigo.acao = False
            self.jogadores[0].acao = False
            self.jogadores[1].acao = False


