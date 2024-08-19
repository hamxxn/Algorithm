from collections import deque
import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
board = []
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]


for i in range(n):
    l = list(map(int, input()))
    board.append(l)

di = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(row, col):
    queue = deque([(row, col, 0)])
    visited[row][col][0] = 1
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            dx, dy = x + di[i][0], y + di[i][1]

            if 0 <= dx < n and 0 <= dy < m and visited[dx][dy][z] == 0:
                # 벽이 있고, 벽을 뚫을 수 있는 경로일 경우
                if board[dx][dy] == 1 and z == 0:
                    visited[dx][dy][1] = visited[x][y][0] + 1
                    queue.append((dx, dy, 1))
                # 벽이 없고, 아직 방문하지 않았다면
                elif board[dx][dy] == 0:
                    visited[dx][dy][z] = visited[x][y][z] + 1
                    queue.append((dx, dy, z))
    return -1


print(bfs(0, 0))
