''' .py com classes referentes a leitura csv 
   e impressão de todas os tiles'''
import csv, sys,os
import pygame as pg

from Configs import Config




#classe feita para gerar o mapa, apartir do arquivo CSV

def load_csv(filename):
    map =[]
    with open(os.path.join(filename)) as data:
        data = csv.reader(data, delimiter = ',')
        for row in data:
            numeros = []
            for i in row:
                numeros.append(int(i))
            map.append(list((numeros)))
    return map

def load_tiles(filename,tileset):
    image = []
    map = load_csv(filename)
    x,y = 0,0
    for row in map:
        x = 0
        for line in row:  
            if  line == 0:
                pass
            else:
                image.append(Tile(tileset[line],x*Config.MapW,y*Config.MapH))        
            x+=1
        y+=1
    return image



#Classe feita para separar os sprites do .png
class TileSet:
	def __init__(self, image):
		self.tiles = image

	def get_tile(self, frame, width, height):
		image = pg.Surface((width, height))
        
        #os tiles lidos, estão na vertical, sendo x = 0 e y = frame * altura
		image.blit(self.tiles, (0, 0), (0, (frame * height), width, height))

		return image


#classe feita para imprimir a tela e/ou obter o retangulo do tile
class Tile:

    def __init__(self,tileImage,posX,posY):
        self.tileImage = tileImage
        self.posX = posX
        self.posY = posY

    #retorna a posição no x e y para adição à lista de colisoes
    def rect (self):

        return (self.posX,self.posY)


    def desenha(self,screen):
        imagem = self.tileImage.convert()
        self.tileImage.set_colorkey((0,0,0))
        screen.blit(self.tileImage,(self.posX,self.posY))