from Configs import *
from Imagens import *



#Nessa classe, estão sendo tratadas de maneira individual 
# os ataques basicos e habilidades

class melee:
    def __init__(self,raio):
        self.cooldown = 0
        self.raio = raio
        self.x = None
        self.y = None

    def sleep(self):
        pass

    def Basica(self,tela,x,y,alvo):
        self.x = x
        self.y = y
        rect = pg.Rect(self.x+32,self.y+20,80,40)
        if rect.colliderect(alvo.hitbox):
            print('hit')


    
    def ataque(self,lista):
        pass

    def colisao(self,alvo) -> bool:
        return ((self.y - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + self.raio>alvo.hitbox[1]) and 
            (self.x + self.raio>alvo.hitbox[0] and 
            self.x - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))
