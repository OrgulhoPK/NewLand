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

    #mob e a duelista
    def Basica(self,x,y,dados):
        
        self.x = x
        self.y = y
        tela = dados[0]
        alvo = dados[1]
        rect = pg.Rect(self.x+32,self.y+20,80,40)
        if rect.colliderect(alvo.hitbox):
            alvo.hit()

            # - - - - - - - - -
            # 1 1 + 0 0 0 0 + -
            # 1 1 0 0 0 0 0 0 -
            # 1 1 + 0 0 0 0 + -
            # - - - - - - - - -
    def BasicaGuaraci():
        pass

        # - - - - - - - - -
        # 1 1 0 + - - - - -
        # 1 1 0 + - - - - -
        # 1 1 0 + - - - - -
        # - - - - - - - - -




    
    def ataque(self,lista):
        pass

    def colisao(self,alvo) -> bool:
        return ((self.y - self.raio< alvo.hitbox[1]+alvo.hitbox[3] and
            self.y + self.raio>alvo.hitbox[1]) and 
            (self.x + self.raio>alvo.hitbox[0] and 
            self.x - self.raio < alvo.hitbox[0]+alvo.hitbox[2]
            ))
