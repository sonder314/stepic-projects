# knight’s move on the chessboard
position = list(input())                                                 # take the knight's posotion
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']                          
chessboard = [[['.'] for _ in range(8)] for _ in range(8)]               # сreate a chessboard
index_i = 8 - int(position[1])                                           # convert indexes to type int
index_j = int(alphabet.index(position[0]))
operations = ['+2', '-2', '+1', '-1']

chessboard[index_i][index_j] = 'N'                                       # mark the knight's position

for i in operations[:2]:                                                 # match operations and indexes
    for j in operations[2:]:
        if 0 <= index_i + int(i) <= 7 and 0 <= index_j + int(j) <= 7:    # mark the knight's move if it doesn't go   
            chessboard[index_i + int(i)][index_j + int(j)] = '*'         # over the edge of the board
        if 0 <= index_i + int(j) <= 7 and 0 <= index_j + int(i) <= 7:
            chessboard[index_i + int(j)][index_j + int(i)] = '*'

for i in chessboard:                                                     # display the chessboard
    for j in i:
        print(*j, end=' ')
    print()
