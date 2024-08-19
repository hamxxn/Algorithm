import sys

sys.setrecursionlimit(10000)
T = int(input())
answer = []
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def checkIs1(row, col):
    for i in range(4):
        x, y = row + di[i][0], col + di[i][1]
        if 0 <= x < N and 0 <= y < M and board[x][y] == 1:
            board[x][y] = 0
            checkIs1(x, y)


for i in range(T):
    total = 0
    M, N, K = map(int, input().split())
    board = []
    for i in range(N):
        board.append([0] * M)

    for i in range(K):
        col, row = map(int, input().split())
        board[row][col] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = 0
                checkIs1(i, j)
                total += 1
    answer.append(total)
for i in range(T):
    print(answer[i])
