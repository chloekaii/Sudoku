from cell import Cell
from sudoku_generator import SudokuGenerator
import pygame, sys
from pygame.locals import *

# scale can be used to adjust game window size properly
scale=1
#window size:
WW=270
WH=270
#Cell size:
cw=WW*scale/9
ch=WH*scale/9
bw=3*cw
#white color

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow= (255,255,0)
red = (255,0,0)
grey = (128,128,128)
black = (0,0,0)




class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    # set to 30 for now; later change to difficulty
    self.difficulty = difficulty
    self.srow = -1
    self.scol = -1
    self.game = SudokuGenerator(width, difficulty)
    
  def draw(self):
    for x in range(0, WW, cw): # draw vertical lines
      pygame.draw.line(self.screen, grey, (x,0),(x,WH))
    for y in range (0, WH, cw): # draw horizontal lines
      pygame.draw.line(self.screen, grey, (0,y), (WW, y))

    ### Draw Major Lines
    for x in range(0, WW, bw): # draw vertical lines
       pygame.draw.line(self.screen, black, (x,0),(x,WH))
    for y in range (0, WH, bw): # draw horizontal lines
       pygame.draw.line(self.screen, black, (0,y), (WW, y))
    
    for i in range(0, WW):
      for j in range(0, WH):
        mycell = Cell(i, j, self.screen,self.game.board[i][j])
        mycell.draw()
 
    
  def select(self, row, col):
    # draw red line on the selected cell
    pygame.draw.line(self.screen, red, (row, col), (row, col + cw)) #horizontal
    pygame.draw.line(self.screen, red, (row + ch, col), (row + ch, col + cw)) #horizontal
    pygame.draw.line(self.screen, red, (row, col), (row + ch, col)) #virtical
    pygame.draw.line(self.screen, red, (row, col + cw), (row + ch, col + cw)) #virtical
    self.srow = row
    self.scol = col
    
    
  def click(self, x, y):
    col=-1
    row=-1
    for i in range(0, WW, cw): # figur out col
      if x >= i and x < i + cw:
        col = i

    for i in range (0, WH, ch): # figur out row
      if y >= i and y < i + ch:
        row = i

    if col > -1 and row > -1:
      #set selected cell in screen
      self.srow = row
      self.scol = col
      #return postion tuple
      return (row, col)
    else:
      return None
    
  def clear(self):
    if self.srow == -1 or self.scol == -1:
      return None
    mycell = Cell(self.srow, self.scol, self.screen)
   
    #find the workable cell and set value to 0
    #game has a list of cells that's workable in reoved_list 
    for i in range (0, len(self.game.removed_list)):
      if self.game.removed_list[i] == (self.srow, self.scol):
        mycell.set_cell_value(0)

    
  def sketch(self, value):
    if self.srow == -1 or self.scol == -1:
      return None
    mycell = Cell(self.srow, self.scol, self.screen)
    mycell.set_sketched_value()
    mycell.draw()
    
  def place_number(self, value): 
    if self.srow == -1 or self.scol == -1:
      return None
    mycell = Cell(self.srow, self.scol, self.screen)
    mycell.set_cell_value()
    mycell.draw()
    
    
  def reset_to_original(self):
    #find the workable cell and scratch sketch flag
    #draw
    for i in range (0, len(self.game.removed_list)):
      (row,col)=self.game.removed_list[i]
      mycell = Cell(row, col, self.screen)
      mycell.sketched_value=0
      mycell.draw()

  def is_full(self):
    #going through workable cells if found zero
    #not full
    #after the loop, no zero found, full and return True
    for i in range (0, len(self.game.removed_list)):
      (row,col)=self.game.removed_list[i]
      mycell = Cell(row, col, self.screen)
      if mycell.value == 0:
        return False
    return True
      
   
  def update_board(self): 
    for i in range (0, len(self.game.removed_list)):
      (row,col)=self.game.removed_list[i]
      mycell = Cell(row, col, self.screen)
      if mycell.sketched_value != 0:
        mycell.set_cell_value(mycell.sketched_value)
        mycell.sketched_value = 0
      mycell.draw()

   
  def find_empty(self): 
    
    for i in range (0, len(self.game.removed_list)):
      (row,col)=self.game.removed_list[i]
      mycell = Cell(row, col, self.screen)
      if mycell.value == 0:
        return (row,col)
      

  def check_board(self): 
    for i in range(0, WW):
      for j in range(0, WH):
        if not self.game.is_valid(i, j, self.game.board[i][j]):
          return False
    
