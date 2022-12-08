from cell import Cell
from board import Board
from sudoku_generator import SudokuGenerator
import pygame,sys
from pygame.locals import *



#window size:
WW=270
WH=270
#Cell size:
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
yellow= (255,255,0)
red = (255,0,0)
grey = (128,128,128)
black = (0,0,0)

def draw_greeting():
    screen = pygame.display.set_mode((WW, WH))
    screen.fill(grey)
    pygame.display.set_caption('Sudoku')

    font = pygame.font.Font(None, 24)
    #font.render returns a surface object with text
    #the get_rect() returns a rect with location infor
    #blit copy text surface to rect area
    easy_img = font.render("Easy", False, red)
    easy_rect=easy_img.get_rect()
    easy_rect.topleft=(30,200)
    medium_img = font.render("Medium", False, red)
    medium_rect=medium_img.get_rect()
    medium_rect.topleft=(90,200)
    hard_img = font.render("Hard", False, red)
    hard_rect=hard_img.get_rect()
    hard_rect.topleft=(160,200)
    screen.blit(easy_img,easy_rect)
    screen.blit(medium_img,medium_rect)
    screen.blit(hard_img,hard_rect)


    title_surface1 = font.render("Welcome to Sudoku", 0, red)
    title_rectangle = title_surface1.get_rect(
        center=(WW// 2, WH // 2 - 25))
    screen.blit(title_surface1, title_rectangle)

    title_surface2 = font.render("Select a Gamemode:", 0, red)
    title_rectangle = title_surface2.get_rect(
        center=(WW // 2, WH // 2))
    screen.blit(title_surface2, title_rectangle)
    pygame.display.update()
    return screen

def draw_won():
    screen = pygame.display.set_mode((WW, WH))
    screen.fill(grey)
    pygame.display.set_caption('Sudoku')

    font = pygame.font.Font(None, 24)
    #font.render returns a surface object with text
    #the get_rect() returns a rect with location infor
    #blit copy text surface to rect area
    won_img = font.render("Game Won!", False, black)
    easy_rect=won_img.get_rect()
    easy_rect.topleft=(90,100)
    
    
    screen.blit(won_img,easy_rect)
    


    title_surface1 = font.render("Exit", 0, red)
    title_rectangle = title_surface1.get_rect(
        center=(WW// 2 - 20, 150))
    screen.blit(title_surface1, title_rectangle)
    pygame.display.update()
    return screen

def draw_over():
    screen = pygame.display.set_mode((WW, WH))
    screen.fill(grey)
    pygame.display.set_caption('Sudoku')

    font = pygame.font.Font(None, 24)
    #font.render returns a surface object with text
    #the get_rect() returns a rect with location infor
    #blit copy text surface to rect area
    over_img = font.render("Game Over! :(", False, black)
    over_rect=over_img.get_rect()
    over_rect.topleft=(90,100)
    
    screen.blit(over_img,over_rect)
    


    title_surface1 = font.render("Exit", 0, red)
    title_rectangle = title_surface1.get_rect(
        center=(WW// 2 - 20, 150))
    screen.blit(title_surface1, title_rectangle)
    pygame.display.update()
    return screen

def key_handler(event):
    if event.key == pygame.K_1:
        kval=1
    elif event.key == pygame.K_2:
        kval=2
    elif event.key == pygame.K_3:
        kval=3
    elif event.key == pygame.K_4:
        kval=4
    elif event.key == pygame.K_5:
        kval=5
    elif event.key == pygame.K_6:
        kval=6
    elif event.key == pygame.K_7:
        kval=7
    elif event.key == pygame.K_8:
        kval=8
    elif event.key == pygame.K_9:
        kval=9
    elif event.key == pygame.K_RETURN:
        kval=10
    else:
        kval=0
    return kval

def play(screen, level):
    # board is only created once for a single play
    #clear previous events
    pygame.event.clear
    board = Board(WW, WH, screen, level)
    screen.fill(grey)
    board.draw()
    pygame.display.update()   
    
    while True:
        done="no"
        #don't do anything unless left mouse click
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
             done="yes"
             break
           elif event.type == pygame.MOUSEMOTION:
              if event.rel[0] > 0:
                #moveing to the right
                continue
              elif event.rel[1] > 0:
                #Mouse moving down
                continue
           elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 or event.button == 2 or event.button == 3 or True:
                    (cx,cy)=pygame.mouse.get_pos()
                    #handle_cell(board,cx,cy)
                    (crow, ccol) = board.click(cx,cy)
                    board.select(crow, ccol)
                    
                    pygame.display.update()
                    pygame.event.clear()
           elif event.type == pygame.MOUSEBUTTONUP:
                  continue
           elif event.type == pygame.MOUSEMOTION:
                  continue
           elif event.type == pygame.KEYDOWN:
              #pass event to key_handler()
              #get keyinput in kval
              kval = key_handler(event)
              if kval == 0:
                 continue
            # kval 10 means "return" is pressed
            # if there is a skeched cell, it needs to commit
              elif kval == 10:
                if board.check_board():
                    board.screen = draw_won()
                    continue
                if board.is_full():
                    board.screen = draw_over()
                    continue
                board.update_board()
              else:
                board.sketch(kval)
                 
               
        if done == "yes":         
          screen.fill(grey)
          break


def main():
    pygame.font.init()
    pygame.init()
    screen=draw_greeting()
   
    while True:
       #draw_game_start(screen)
        pygame.display.update()
        event = pygame.event.wait()
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
               (cx,cy) = pygame.mouse.get_pos()
               if (cy >= 30 and cy < 100):
                  play(screen,30)
                  screen=draw_greeting()
                  pygame.display.update()
               if (cy >= 100 and cy < 170):
                  play(screen,40)
                  screen=draw_greeting
                  pygame.display.update()
               if (cy >= 170):
                    play(screen,50)
                    screen=draw_greeting()
                    pygame.display.update()

if __name__ == '__main__':
    main()

