#coding:utf-8
from game import Game

# Initialization parameters
win_res = (1500, 1000) # W,H, must be ints
gridsize = 20 # number of pixels per unit, must be an int
fps_max = 5 # speed of the snake 10 -> 10 cases per second

# Initialize the game
game = Game(win_res,gridsize,fps_max)

# Run the game
game.run_game()
