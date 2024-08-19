from collections import deque
import sys

sys.setrecursionlimit(100000)

n = int(input())
board = []

for i in range(n):
    l = list(map(int, input().split()))
    board.append(l)

di = [[1, 0], [-1, 0], [0, 1], [0, -1]]

m = max(map(max, board))
result = 0


def reset(h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] <= h:
                visited[i][j] = True
    return visited


def bfs(row, col):

    queue = deque([(row, col)])
    visited[row][col] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + di[i][0], y + di[i][1]
            if 0 <= dx < n and 0 <= dy < n:
                if visited[dx][dy] == False:
                    visited[dx][dy] = True
                    queue.append((dx, dy))


for h in range(0, m + 1):
    r = 0
    visited = reset(h)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                r += 1
                bfs(i, j)
    result = max(result, r)

print(result)
