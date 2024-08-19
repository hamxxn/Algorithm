from collections import deque

m, n = map(int, input().split())
board = []
queue = deque()
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]
count = 0
tom = 0

for i in range(n):
    e = list(map(int, input().split()))
    for j in range(m):
        if e[j] == 1:
            queue.append([i, j])
        elif e[j] == 0:
            tom += 1
    board.append(e)


if tom == 0:
    print(0)
else:
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + di[i][0], y + di[i][1]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                tom -= 1
                queue.append([nx, ny])
    if tom != 0:
        print(-1)
    else:
        Max = 0
        for i in range(n):
            if Max < max(board[i]):
                Max = max(board[i])
        print(Max - 1)
