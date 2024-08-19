import sys

sys.setrecursionlimit(100000)

n = int(input())
board = []
for i in range(n):
    l = list(map(int, input().split()))
    board.append(l)

visit = [[0 for _ in range(n)] for _ in range(n)]
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(row, col):
    if visit[row][col] != 0:
        return visit[row][col]
    visit[row][col] = 1
    for i in range(4):
        dx, dy = row + di[i][0], col + di[i][1]
        if 0 <= dx < n and 0 <= dy < n:
            if board[dx][dy] > board[row][col]:
                visit[row][col] = max(visit[row][col], dfs(dx, dy) + 1)
    return visit[row][col]


for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            dfs(i, j)
answer = 0
for i in range(n):
    answer = max(answer, max(visit[i]))
print(answer)
