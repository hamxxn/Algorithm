r, c, m = map(int, input().split())
board = [[0 for col in range(c)] for row in range(r)]
total = 0
for i in range(m):
    row, col, s, d, z = map(int, input().split())
    board[row - 1][col - 1] = [z, s, d]


def up(row, col, s):
    if board[i][0] - s < 0:
        c = board[i][0]
        board[i][0] = 0
        board[i][3] = 2
        down(i, s - c)
    else:
        board[i][0] -= s


def down(row, col, s):
    if s + board[i][0] > r - 1:
        ch = board[i][0]
        board[i][0] = r - 1
        board[i][3] = 1
        up(i, s - (r - 1 - ch))
    else:
        board[i][0] += s


def right(row, col, s):
    if s + board[i][1] > c - 1:
        ch = board[i][1]
        board[i][1] = c - 1
        board[i][3] = 4
        left(i, s - (c - 1 - ch))
    else:
        board[i][1] += s


def left(row, col, s):
    if board[i][1] - s < 0:
        c = board[i][1]
        board[i][1] = 0
        board[i][3] = 3
        right(i, s - c)
    else:
        board[i][1] -= s


def change():
    for i in range(r):
        for j in range(c):
            if board[i][j][0] != 0:
                if board[i][j][1] == 1:
                    up(i, j, board[i][j][1])
                elif board[i][j][1] == 2:
                    down(i, j, board[i][j][1])
                elif board[i][j][1] == 3:
                    right(i, j, board[i][j][1])
                elif board[i][j][1] == 4:
                    left(i, j, board[i][j][1])


for i in range(c):
    for j in range(m):
        if board[i][j][0] != 0:
            total += board[i][j][0]
            board[i][j][0] = 0
            break
    change()
