import pygame as pg
import random
import math
import time
import sys
from typing import List
from Configs import Config

pg.init()
    

class Jogador:
    def __init__(self, x, y, widght, height):
        #atualização da posicao
        self.x = x
        self.y = y
        #posicao
        self.widght = widght 
        self.height = height

    def main(self, display):
        pg.draw.rect(display, (255,0,0), (self.x,self.y, self.widght,self.height))

player = Jogador(400,300,32,32)


display_scroll = [0,0]
display = pg.display.set_mode((Config.S_HEIGHT,Config.S_WIDHT))
clock = pg.time.Clock()
while True:
    display.fill((Config.COR_Tela))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            pg.QUIT


    keys = pg.key.get_pressed()
    pg.draw.rect(display, (255,255,255),(Config.Player_y-display_scroll[0],Config.Player_x-display_scroll[1],16,16))

    if keys[pg.K_a]:
        display_scroll[0] += 2
    if keys[pg.K_d]:
        display_scroll[0] -= 2
    if keys[pg.K_w]:
        display_scroll[1] += 2
    if keys[pg.K_s]:
        display_scroll[1] -= 2

    player.main(display)

    clock.tick(60)
    pg.display.update()


    #teste