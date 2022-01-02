position = list(input())
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chessboard = [[['.'] for _ in range(8)] for _ in range(8)]
ind_i = 8 - int(position[1])
ind_j = int(alph.index(position[0]))
operations = ['+2', '-2', '+1', '-1']

chessboard[ind_i][ind_j] = 'N'

for i in operations[:2]:
    for j in operations[2:]:
        if 0 <= ind_i + int(i) <= 7 and 0 <= ind_j + int(j) <= 7:
            chessboard[ind_i + int(i)][ind_j + int(j)] = '*'
        if 0 <= ind_i + int(j) <= 7 and 0 <= ind_j + int(i) <= 7:
            chessboard[ind_i + int(j)][ind_j + int(i)] = '*'

for i in chessboard:
    for j in i:
        print(*j, end=' ')
    print()