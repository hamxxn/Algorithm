from collections import deque

m, n = map(int, input().split())
board = []
queue = deque([])
visited = [[False for _ in range(m)] for _ in range(n)]


for i in range(n):
    l = list(map(int, input().split()))
    board.append(l)

di = [[1, 0], [-1, 0], [0, 1], [0, -1]]

if not any(0 in row for row in board):
    print(0)
else:
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                visited[i][j] = True
            elif board[i][j] == 1:
                visited[i][j] = True
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + di[i][0], y + di[i][1]
            if 0 <= dx < n and 0 <= dy < m:
                if visited[dx][dy] == False:
                    visited[dx][dy] = True
                    board[dx][dy] = board[x][y] + 1
                    queue.append((dx, dy))

    if any(0 in row for row in board):
        print(-1)
    else:
        print(max(map(max, board)) - 1)
