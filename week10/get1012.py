import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
t = int(input())
for z in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    di = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(x, y):
        visited[x][y] = True
        for i in range(4):
            dx, dy = x + di[i][0], y + di[i][1]
            if (
                0 <= dx < m
                and 0 <= dy < n
                and board[dx][dy] == 1
                and visited[dx][dy] == False
            ):
                dfs(dx, dy)

    result = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1 and visited[i][j] == False:
                dfs(i, j)
                result += 1
    print(result)
