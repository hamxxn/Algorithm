from collections import deque

n, m = map(int, input().split())
board = []
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    l = list(map(int, input()))
    board.append(l)
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(row, col):
    queue = deque([(row, col)])
    visited[row][col] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + di[i][0], y + di[i][1]
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == False and not board[dx][dy] == 0:
                    board[dx][dy] = board[x][y] + 1
                    visited[dx][dy] = True
                    queue.append((dx, dy))


bfs(0, 0)

print(board[n - 1][m - 1])
