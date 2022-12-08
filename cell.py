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
cw=30
ch=30
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
    self.selected=0  
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
    if self.sketched_value != 0:
      number_color = green
      numberimage = font.render(str(self.sketched_value), False, number_color)
      numberrect=numberimage.get_rect()
      numberrect.topleft=(self.col*30, self.row*30)
      # copy numberimage to screen at location decided by value in tuple (row, col)
      self.screen.blit(numberimage, numberrect)
    else:
      number_color = black
      numberimage = font.render(str(self.value), False, number_color)
      numberrect=numberimage.get_rect()
      numberrect.topleft=(self.col*30 + 5, self.row*30 + 5)
    # copy numberimage to screen at location decided by value in tuple (row, col)
      self.screen.blit(numberimage, numberrect)
    col = self.col
    row = self.row
    if self.selected == 1:
       pygame.draw.line(self.screen, red, (col*ch, row*ch), (col*ch, row*cw + cw)) #horizontal
       pygame.draw.line(self.screen, red, (col*ch + ch, row*ch), (col*ch + ch, row*cw + cw)) #horizontal
       pygame.draw.line(self.screen, red, (col*ch, row*ch), (col*ch + ch, row*cw)) #virtical
       pygame.draw.line(self.screen, red, (col*ch, row*ch + cw), (col*ch + ch, row*cw + cw)) #virtical
       
    pygame.display.update()
    return


