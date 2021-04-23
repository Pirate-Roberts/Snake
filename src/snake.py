#coding:utf-8
import pygame
import random

class Snake:
    """
    
    """
    UP = (0,-1)
    DOWN = (0,1)
    LEFT = (-1,0)
    RIGHT = (1,0)

    def __init__(self,game):
        self.game = game
        self.positions = [((self.game.window.grid_width//2)*self.game.window.grid_size,(self.game.window.grid_height//2)*self.game.window.grid_size)]
        self.length = 1
        self.direction = random.choice([Snake.UP,Snake.DOWN,Snake.LEFT,Snake.RIGHT])
        self.colors = []
        self.add_colors()
        self.draw()

    def move(self):
        new = (self.positions[0][0]+self.direction[0]*self.game.window.grid_size,self.positions[0][1]+self.direction[1]*self.game.window.grid_size)
        if self.length > 4 and new in self.positions:
            self.reset()
        elif new[0]<0 or new[0]>self.game.window.win_width or new[1]<0 or new[1]>self.game.window.win_height:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def turn(self,direction):
        if self.length>1 and (direction[0]*-1,direction[1]*-1)==self.direction:
            self.direction = self.direction
        else:
            self.direction = direction

    def add_colors(self):
        c = ()
        for i in range(3):
            c = c + (random.randrange(256),)
        self.colors.append(c)

    def stream_color(self):
        pass

    def eat(self):
        if self.game.food.position in self.positions:
            self.length += 1
            self.add_colors()
            self.game.food.generate_new()

    def reset(self):
        self.positions = [((self.game.window.grid_width//2)*self.game.window.grid_size,(self.game.window.grid_height//2)*self.game.window.grid_size)]
        self.length = 1
        self.direction = random.choice([Snake.UP,Snake.DOWN,Snake.LEFT,Snake.RIGHT])
        self.colors = []
        self.add_colors()
        self.draw()
        self.game.food.generate_new()

    def draw(self):
        for i,position in enumerate(self.positions):
            r = pygame.Rect(position[0],position[1],self.game.gridsize,self.game.gridsize)
            pygame.draw.rect(self.game.window.screen,self.colors[i],r)

    def keys_handling(self,key_event):
        if key_event == pygame.K_z:
            self.turn(Snake.UP)
        elif key_event == pygame.K_s:
            self.turn(Snake.DOWN)
        elif key_event == pygame.K_q:
            self.turn(Snake.LEFT)
        elif key_event == pygame.K_d:
            self.turn(Snake.RIGHT)

# This part of code is for debuging purpose
if __name__ == '__main__':
    pass