#Sudoku_game_gui.py
import pygame
from Sudoku_game import solve, valid
import time
pygame.font.init()

class Grid:
     board = [
          [7,8,0,4,0,0,1,2,0],
          [6,0,0,0,7,5,0,0,9],
          [0,0,0,6,0,1,0,7,8],
          [0,0,7,0,4,0,2,6,0],
          [0,0,1,0,5,0,9,3,0],
          [9,0,4,0,6,0,0,0,5],
          [0,7,0,3,0,0,0,1,2],
          [1,2,0,0,0,7,4,0,0],
          [0,4,9,2,0,6,0,0,7]
     ]

     def __init__(self, rows, columns, width, height):
          self.rows = rows
          self.columns = columns
          self.cubes = [[Cube(self.board[x][y], x,y,width, height) for y in range(columns)] for x in range(rows)]
          self.width = width
          self.height = height
          self.model = None
          self.selected = None

     def update_model(self):
          self.model = [[self.cubes[i][j].value for j in range(self.columns)] for i in range(self.rows)]
     
     def place(self,val):
          row, column = self.selected
          if self.cubes[row][column].value ==0:
               self.cubes[row][column].set(val)
               self.update_model()

               if valid(self.model, val, (row,column)) and solve(self.model):
                    return True
               else:
                    self.cubes[row][column].set(0)
                    self.cubes[row][column].set_temp(0)
                    self.update_model()
                    return False
     
     def sketch(self,val):
          row, column = self.selected
          self.cubes[row][column].set_temp(val)
     
     def draw(self,win):
          #Draw Grid Line
          gap = self.width/9
          for x in range(self.rows+1):
               if x % 3 == 0 and x != 0:
                    thick = 4
               else:
                    thick = 1
               pygame.draw.line(win, (0,0,0), (0, x*gap), (self.width, x*gap), thick)
               pygame.draw.line(win, (0,0,0), (x*gap,0), (x*gap, self.height), thick)

          #Draw Cubes
          for x in range(self.rows):
               for y in range(self.columns):
                    self.cubes[x][y].draw(win)
     
     def select(self, row, column):
          #Reset all other
          for x in range(self.rows):
               for y in range(self.columns):
                    self.cubes[x][y].selected = False
          self.cubes[row][column].selected = True # the cubes are non-number
          self.selected = (row, column)

     def clear(self):
          row, column = self.selected()
          if self.cubes[row][column].value == 0:
               self.cubes[row][column].set_temp(0)
     
     def click(self, position):
          """
          param: ros
          return: (row,column)
          """

          if position[0] < self.width and position[1] < self.height:
               gap = self.width/9
               x = position[0] // gap
               y = position[1] // gap
               return (int(y), int(x))
          else:
               return None
     
     def is_finished(self):
          for x in range(self.rows):
               for y in range(self.columns):
                    if self.cubes[x][y].value == 0:
                         return False
          return True
     
class Cube:
     rows = 9
     columns = 9

     def __init__(self, value, row, column, width, height):
          self.value = value
          self.temp = 0
          self.row = row
          self.column = column
          self.width = width
          self.height = height
          self.selected = False

     def draw(self, win):
          fnt = pygame.font.SysFont("comicsans", 40)
          
          gap = self.width / 9
          x = self.column * gap
          y = self.row * gap

          if self.temp != 0 and self.value == 0:
               text = fnt.render(str(self.temp), 1, (128,128,128))
               win.blit(text, (x+5, y+5))
          elif not(self.value == 0):
               text = fnt.render(str(self.value), 1, (0, 0, 0))
               win.blit(text, (x + (gap/2 - text.get_width()/2), y + (gap/2 - text.get_height()/2)))

          if self.selected:
               pygame.draw.rect(win, (255,0,0), (x,y,gap,gap), 3)
     
     def set(self,val):
          self.value = val
     
     def set_temp(self,val):
          self.temp = val

def redraw_window(win, board, time, strikes):
     win.fill((255,255,255))

     #Draw time
     fnt = pygame.font.SysFont("comicsans", 40)
     text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
     win.blit(text,(540-160,560))

     #Draw Strikes
     text = fnt.render("X " * strikes, 1, (255,0,0) )
     win.blit(text,(20,560))
     #Draw grid and board
     board.draw(win)

def format_time(secs):
     sec = secs%60
     minute = secs//60
     hour = minute//3600

     mat = str(hour) + ":" + str(minute) + ":" + str(sec)
     return mat

def main():
     win = pygame.display.set_mode((540,600))
     pygame.display.set_caption("Sudoku")
     board = Grid(9, 9, 540, 540)
     key = None
     run = True
     start = time.time()
     strikes = 0
     while run:

          play_time = round(time.time() - start)

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    run = False
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                         key = 1
                    if event.key == pygame.K_2:
                         key = 2
                    if event.key == pygame.K_3:
                         key = 3
                    if event.key == pygame.K_4:
                         key = 4
                    if event.key == pygame.K_5:
                         key = 5
                    if event.key == pygame.K_6:
                         key = 6
                    if event.key == pygame.K_7:
                         key = 7
                    if event.key == pygame.K_8:
                         key = 8
                    if event.key == pygame.K_9:
                         key = 9
                    if event.key == pygame.K_DELETE:
                         board.clear()
                         key = None
                    if event.key == pygame.K_RETURN:
                         i, j = board.selected
                         if board.cubes[i][j].temp != 0:

                              if board.place(board.cubes[i][j].temp):
                                   print("Success")
                              else:
                                   print("Wrong")
                                   strikes += 1
                              key = None

                              if board.is_finished():
                                   print("Game over")
                                   run = False

               if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = board.click(pos)
                    if clicked:
                         board.select(clicked[0], clicked[1])
                         key = None

          if board.selected and key != None:
               board.sketch(key)

          redraw_window(win, board, play_time, strikes)
          pygame.display.update()


main()
pygame.quit()
