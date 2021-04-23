#coding:utf-8
import pygame
import sys
from window import Window
from snake import Snake
from food import Food

class Game():
    """
    
    """

    def __init__(self,win_res,gridsize,fps_max):
        pygame.init()
        self.gridsize = gridsize
        self.clock = pygame.time.Clock()
        self.window = Window(win_res,self.gridsize)
        self.snake = Snake(self)
        self.food = Food(self.window)
        self.fps_max = fps_max
    
    def run_game(self):

        while True:
            # Program body

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Fermeture du jeu, Goodbye!")
                    pygame.quit()
                    sys.exit()
                else:
                    if event.type == pygame.KEYDOWN:
                        self.snake.keys_handling(event.key)
            
            self.window.screen.blit(self.window.checkerboard,(0,0))
            self.snake.move()
            self.snake.draw()
            self.snake.eat()
            self.food.add_color()
            self.food.draw()
            pygame.display.update()
            self.clock.tick(self.fps_max)

 # This part of code is for debuging purpose
if __name__ == '__main__':
    game = Game((1500,1000),50,60)    
    game.run_game()                 