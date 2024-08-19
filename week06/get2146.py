from collections import deque

n = int(input())
board = []
visited = [[0] * n for _ in range(n)]
di = [[1, 0], [-1, 0], [0, 1], [0, -1]]
num = 1
for i in range(n):
    board.append(list(map(int, input().split())))


# 대륙 구분
def bfs(row, col):
    queue = deque([[row, col]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + di[i][0], y + di[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                board[nx][ny] = num
                queue.append([nx, ny])


def bfs2(number):
    getDi = [[-1] * n for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == number:
                queue.append([i, j])
                getDi[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + di[i][0], y + di[i][1]
            if 0 <= nx < n and 0 <= ny < n:
                if not board[nx][ny] and getDi[nx][ny] == -1:
                    getDi[nx][ny] = getDi[x][y] + 1
                    queue.append([nx, ny])
                elif board[nx][ny] != 0 and board[nx][ny] != number:
                    return getDi[x][y]
    return 100000


for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            visited[i][j] = 1
            board[i][j] = num
            bfs(i, j)
            num += 1


getMin = 1000000

for i in range(1, num):
    getMin = min(getMin, bfs2(i))

print(getMin)
