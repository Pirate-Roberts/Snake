#coding:utf-8
import pygame
import random

class Food:
    """
    
    """

    def __init__(self,window):
        self.window = window
        self.generate_new()
        
    def generate_new(self):
        self.position = (random.randrange(self.window.grid_width)*self.window.grid_size,random.randrange(self.window.grid_height)*self.window.grid_size)
        self.add_color()
        self.draw()

    def draw(self):
        r = pygame.Rect(self.position[0],self.position[1],self.window.grid_size,self.window.grid_size)
        pygame.draw.rect(self.window.screen,self.color,r)

    def add_color(self):
        c = ()
        for i in range(3):
            c = c + (random.randrange(256),)
        self.color = c