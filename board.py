from cell import Cell
import sudoku_generator
import pygame, sys
from pygame.locals import *

# scale can be used to adjust game window size properly
scale=1
#window size:
WW=270
WH=270
#Cell size:
cw=30
ch=30
bw=90
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
    if type(difficulty) is str:
      if difficulty.upper == 'EASY':
        difficulty=30
      if difficulty.upper == 'MEDIUM':
        difficulty=40
      if difficulty.upper == 'HARD':
        difficulty=50
    self.difficulty = difficulty
    self.width = width
    self.height = height
    self.screen = screen
    self.srow = -1
    self.scol = -1
    self.gameboard = sudoku_generator.generate_sudoku(width//cw, 30)
    self.cell_dict={}
    
  def draw(self):
    self.screen.fill(grey)
    for x in range(0, WW, cw): # draw horizontal lines
      pygame.draw.line(self.screen, grey, (x,0),(x,WW))
    for y in range (0, WH, cw): # draw virtical lines
      pygame.draw.line(self.screen, grey, (0,y), (WH, y))

    ### Draw Major Lines
    for x in range(0, WW, bw): # draw vertical lines
       pygame.draw.line(self.screen, black, (x,0),(x,WH))
    for y in range (0, WH, bw): # draw horizontal lines
       pygame.draw.line(self.screen, black, (0,y), (WW, y))
    # Draw numbers
    # prepare board number arrays
    if len(self.cell_dict) < 81:
      for i in range(0, 9):
        for j in range(0, 9):
          mycell = Cell(self.gameboard.board[i][j],i, j, self.screen)
          self.cell_dict[(i,j)] = mycell
          mycell.draw()
    else:
      for i in range(0, 9):
        for j in range(0, 9):
          mycell = self.cell_dict[(i,j)]
          mycell.draw()
    
  def select(self, row, col):
    # draw red line on the selected cell
    #only select when no other is selected
    found=False
    for i in range(0, len(self.gameboard.removed_list)):
      #clear selected bit
      self.cell_dict[self.gameboard.removed_list[i]].selected=0
      if self.gameboard.removed_list[i] == (row, col):
        found=True
      
    if not found:
      return
    # found that (row, col) is workable
    # high light it if not alrady marked
    
    self.srow = row
    self.scol = col
    # register the cell as marked
    self.cell_dict[(row, col)].selected=1
    self.draw()
    return
    
  def click(self, x, y):
    col=-1
    row=-1
    for i in range(0, WW, cw): # figur out col
      if x >= i and x < i + cw:
        col = i//cw

    for i in range (0, WH, ch): # figur out row
      if y >= i and y < i + ch:
        row = i//ch

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
    for i in range (0, len(self.gameboard.removed_list)):
      if self.gameboard.removed_list[i] == (self.srow, self.scol):
        mycell.set_cell_value(0)

    
  def sketch(self, value):
    if self.srow == -1 or self.scol == -1:
      return None
    mycell = self.cell_dict[(self.srow,self.scol)]
    mycell.set_sketched_value(value)
    mycell.draw()
    
  def place_number(self, value): 
    if self.srow == -1 or self.scol == -1:
      return None
    mycell = Cell(self.srow, self.scol, self.screen)
    mycell.set_cell_value(value)
    mycell.draw()
    
    
  def reset_to_original(self):
    #find the workable cell and scratch sketch flag
    #draw
    for i in range (0, len(self.gameboard.removed_list)):
      (row,col)=self.gameboard.removed_list[i]
      mycell = Cell(row, col, self.screen)
      mycell.sketched_value=0
      mycell.draw()

  def is_full(self):
    #going through workable cells if found zero
    #not full
    #after the loop, no zero found, full and return True
    for i in range (0, len(self.gameboard.removed_list)):
      (row,col)=self.gameboard.removed_list[i]
      mycell = self.cell_dict[(row,col)]
      if mycell.value == 0:
        return False
    return True
      
   
  def update_board(self): 
    for i in range (0, len(self.gameboard.removed_list)):
      (row,col)=self.gameboard.removed_list[i]
      mycell = self.cell_dict[(row,col)]
      if mycell.sketched_value != 0:
        mycell.set_cell_value(mycell.sketched_value)
        mycell.sketched_value = 0
    self.draw()

   
  def find_empty(self): 
    
    for i in range (0, len(self.gameboard.removed_list)):
      (row,col)=self.gameboard.removed_list[i]
      mycell = Cell(row, col, self.screen)
      if mycell.value == 0:
        return (row,col)
      

  def check_board(self): 
    for i in range(0, 9):
      for j in range(0, 9):
        if not self.gameboard.is_valid(i, j, self.cell_dict[(i, j)]):
          return False
    return False
    
