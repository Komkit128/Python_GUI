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

def solve(board):
     find = find_empty(board)
     if not find:
          return True
     else:
          row, column = find
     
     for x in range(1,10):
          if valid(board, x, (row,column) ):
               board[row][column] = x

               if solve(board):
                    return True
               
               board[row][column] = 0
     return False

     


def valid(board, number, position):
     # Check row
     for y in range(len(board)):
          if board[position[0]][y] == number and position[1] != y:
               return False

     # Check column
     for x in range(len(board)):
          if board[x][position[1]] == number and position[0] != x:
               return False

     # Check box: #position = row, column
     box_x = position[1] // 3 
     box_y = position[0] // 3

     for x in range(box_y*3,box_y*3 + 3):
          for y in range(box_x*3, box_x*3+3):
               if board[x][y] == number and (x,y) != position:
                    return False
     return True

def print_board(board):
     for x in range(len(board)):
          if x % 3 == 0 and x != 0:
               print("- - - - - - - - - - - -")

          for y in range(len(board[0])):
               if y%3 == 0 and y!= 0:
                    print(" | ", end="")

               if y == 8:
                    print(board[x][y])
               else:
                    print(str(board[x][y]) + " ", end="")

def find_empty(board):
     for x in range(len(board)):
          for y in range(len(board)):
               if board[x][y] == 0:
                    return (x,y) # row,column
     #If not empty
     return None



#Run function
print_board(board)
solve(board)
print("---------------------------------------------------")
print_board(board)




