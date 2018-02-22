file  = open("sudokuboards.txt", "r")

a = file.readlines()

board = [["0" for x in range(9)] for y in range(9)]

for i in range(len(a) - 1):
  for j in range(len(a[i]) - 1):
    #print "{}, {}".format(i,j)
    board[i][j] = a[i][j]
print board