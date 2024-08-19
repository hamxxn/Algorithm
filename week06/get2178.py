from collections import deque

n, m = map(int, input().split())
board = []
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = []
count = 1
for i in range(n):
    visited.append(list([False] * m))
    board.append(list(map(int, " ".join(input().split()))))


queue = deque([[0, 0]])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + di[i][0], y + di[i][1]
        if (0 <= nx < n) and (0 <= ny < m) and (board[nx][ny] == 1):
            board[nx][ny] = board[x][y] + 1
            queue.append([nx, ny])
            visited[nx][ny] = True


print(board[n - 1][m - 1])
