#coding:utf-8
import pygame

class Window():
    """
    
    """
    bg_color = (255,255,255)

    def __init__(self,win_res,gridsize):
        pygame.display.set_caption("SNAKE ML")
        self.grid_size = gridsize
        self.grid_width = int(win_res[0]//self.grid_size)
        self.grid_height = int(win_res[1]//self.grid_size)
        self.win_width = self.grid_width*self.grid_size
        self.win_height = self.grid_height*self.grid_size
        self.screen = pygame.display.set_mode((self.win_width,self.win_height)) # pygame.Surface
        self.checkerboard = pygame.Surface(self.screen.get_size()).convert()
        self.draw_grid()
    
    def draw_grid(self):
        """
        Draw grid/checkerboard on displayed surface.
        """
        for y in range(0,self.grid_height):
            for x in range(0,self.grid_width):
                r = pygame.Rect((x*self.grid_size,y*self.grid_size),(self.grid_size,self.grid_size))
                if (x+y)%2 == 0:
                    pygame.draw.rect(self.checkerboard,(176,255,250),r)
                else:
                    pygame.draw.rect(self.checkerboard,(255,250,176),r)

# This part of code is for debuging purpose
if __name__ == '__main__':
    window = Window((1500,1000),5)
    print(5.2//3)
    print(window.grid_height)