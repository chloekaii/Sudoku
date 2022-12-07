import sys, pygame
from pygame.locals import *
import pygame.font
from sudoku_generator import SudokuGenerator

FPS = 10
scale=1
#window size:
WW=270
WH=270
#Cell size:
cw=WW*scale/9
ch=WH*scale/9
#white color

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow= (255,255,0)
red = (255,0,0)
grey = (128,128,128)
black = (0,0,0)

class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value 
    self.row = row
    self.col = col
    self.screen=screen
    self.sketched_value=0  
  def set_cell_value(self, value):  
    # Setter for this cell’s value  
    self.value = value
 
  def set_sketched_value(self, value): 
    # Setter for this cell’s sketched value  
    self.sketched_value = value
 
  def draw(self):
    # Draws this cell, along with the value inside it.  
    # If this cell has a nonzero value, that value is displayed.    
    # Otherwise, no value is displayed in the cell.  
    # The cell is outlined red if it is currently selected.  
    pygame.init()
    font = pygame.font.Font(None, 24)
    #draw lines later

    if self.sketched_value != 0:
      number_color = grey
    else:
      number_color = black
    
    pygame.draw.line(self.screen, grey, (self.col, self.row), (self.col + cw, self.row))
    pygame.draw.line(self.screen, grey, (self.col, self.row), (self.col, self.row + ch))
    pygame.draw.line(self.screen, grey, (self.col + cw, self.row), (self.col + cw, self.row + ch))
    pygame.draw.line(self.screen, grey, (self.col, self.row + ch), (self.col + cw, self.row + ch))
    
    # bind the number/value with a display image numberimage
    # True just means not to Cap the initial letter
    numberimage = font.render(str(self.value), True, number_color)
    # copy numberimage to screen at location decided by value in tuple (row, col)
    self.screen.blit(numberimage, (self.row + cw/4, self.col + ch/4))
    #flip refresh the changed image in screen
    pygame.display.flip()


