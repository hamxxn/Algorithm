import sys

sys.setrecursionlimit(100000)
board = []
check = []
for i in range(9):
    l = list(map(int, input().split()))
    if 0 in l:
        for j in range(9):
            if l[j] == 0:
                check.append([i, j])
    board.append(l)


def checkRowCol(row, col, a):
    for i in range(9):
        if board[row][i] == a or board[i][col] == a:
            return False
    return True


def check3X3(row, col, a):
    x, y = row // 3, col // 3
    for i in range(3):
        for j in range(3):
            if board[x * 3 + i][y * 3 + j] == a:
                return False
    return True


def backtrack(idx):
    if idx == len(check):
        for i in range(9):
            print(*board[i])
        exit(0)

    row, col = check[idx][0], check[idx][1]

    for i in range(10):
        if checkRowCol(row, col, i):
            if check3X3(row, col, i):
                board[row][col] = i
                backtrack(idx + 1)
                board[row][col] = 0


backtrack(0)
