n = int(input())
board = []
for i in range(n):
    l = list(input())
    board.append(l)
disable = [[False for _ in range(n)] for _ in range(n)]
normal = [[False for _ in range(n)] for _ in range(n)]
di = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(x, y):
    disable[x][y] = True
    normal[x][y] = True
    for i in range(4):
        dx, dy = x + di[i][0], y + di[i][1]
        if 0 <= dx < n and 0 <= dy < n and normal[dx][dy] == False:
            if board[x][y] == board[dx][dy]:
                dfs(dx, dy)


for i in range(n):
    for j in range(n):
        if normal[i][j] == False:
            dfs(i, j)
