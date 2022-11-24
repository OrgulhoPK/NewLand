import pygame,sys
from Configs import *
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


class Pathfinder:

    def __init__(self,matriz):
        #setup
        self.matriz = matriz
        self.grid = Grid(matrix= matriz)
        self.select_surf = pygame.image.load('selection.png').convert_alpha()
        #pathfinder
        self.path = []
        #Roomba
        self.roomba = pygame.sprite.GroupSingle(Roomba(self.empty_path))
    
    def empty_path(self):
        self.path=[]

    def draw_active_cell(self,screen):
        mouse_pos  = pygame.mouse.get_pos()
        row = mouse_pos[1] // 32
        col = mouse_pos[0] // 32
        current_cell_value = self.matriz[row][col]
        if current_cell_value == 1:
            rect = pygame.Rect((col*32,row *32),(32,32))
            screen.blit(self.select_surf,rect)
    def create_path(self):
        #start
        start_x,start_y = self.roomba.sprite.get_coord()
        start = self.grid.node(start_x,start_y)


        #end
        mouse_pos  = pygame.mouse.get_pos()
        end_y,end_x = mouse_pos[1] // 32,mouse_pos[0] // 32
        end  = self.grid.node(end_x,end_y)


        # path
        finder = AStarFinder(diagonal_movement= DiagonalMovement.always)
        self.path,_ = finder.find_path(start,end,self.grid)
        self.grid.cleanup()
        print(self.path)
        self.roomba.sprite.set_path(self.path)



    def draw_path(self,screen):
        if self.path:
            points = []
            for point in self.path:
                x = (point[0] *32) +16  
                y = (point[1] * 32) + 16

                points.append((x,y))
                pygame.draw.circle(screen,'#4a4a4a',(x,y),2)
            pygame.draw.lines(screen,'#4a4a4a',False,points,5)

    def update(self,screen):
        self.draw_active_cell(screen)
        self.draw_path(screen)

        self.roomba.update()
        self.roomba.draw(screen)

class Roomba(pygame.sprite.Sprite):
    def __init__(self,empty_path):
        #basic
        super().__init__()
        self.image = pygame.image.load('roomba.png').convert_alpha()
        self.rect =  self.image.get_rect(center = (60,60))
        self.empty_path = empty_path
        #movement
        self.pos = self.rect.center
        self.speed = 0.6
        #path
        self.path = []
        self.direction = pygame.math.Vector2(0,0)
        self.collision_rects = []
    
    def get_coord(self):
        col,rol = self.rect.centerx //32,self.rect.centery//32
        return(col,rol)
    def set_path(self,path):
        self.path = path
        self.create_collision_rects()
        self.get_direction()
    
    def create_collision_rects(self):
        if self.path:
            self.collision_rects =[]
            for point in self.path:
                x = (point[0] * 32) + 16
                y = (point[1] * 32) + 16
                rect = pygame.Rect((x-2,y-2),(4,4))
                self.collision_rects.append(rect)

    def get_direction(self):
        if self.collision_rects:
            start = pygame.math.Vector2(self.pos)
            end = pygame.math.Vector2(self.collision_rects[0].center)
            self.direction = (end-start).normalize()
        else:
            self.direction = pygame.math.Vector2(0,0)
            self.path = []

    def check_collisions(self):
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(self.pos):
                    del self.collision_rects[0]
                    self.get_direction() 
        else:
            self.empty_path()

    def update(self):
        self.pos += self.direction * self.speed
        self.check_collisions()
        self.rect.center = self.pos

