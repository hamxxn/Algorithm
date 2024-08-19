from collections import deque
import sys

sys.setrecursionlimit(100000)
n = int(input())
board = []
fish = [0 for _ in range(7)]
row, col = 0, 0
di = [[-1, 0], [0, -1], [1, 0], [0, 1]]
size = 2
answer = 0
eat = 0

# 물고기
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 9:
            l[j] = 0
            row, col = i, j
        elif 1 <= l[j] <= 6:
            fish[l[j]] += 1
    board.append(l)


def bfs(r, c):
    global row, col, eat
    fish_list = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[r][c] = True
    queue = deque([(r, c, 0)])

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            dx, dy = x + di[i][0], y + di[i][1]
            if (
                0 <= dx < n
                and 0 <= dy < n
                and visited[dx][dy] == False
                and board[dx][dy] <= size
            ):
                visited[dx][dy] = True
                if 0 < board[dx][dy] < size:
                    fish_list.append((dist + 1, dx, dy))
                queue.append((dx, dy, dist + 1))
    # 가장 가까운 물고기 찾기
    if fish_list:
        fish_list.sort()
        dist, min_x, min_y = fish_list[0]
        eat += 1
        fish[board[min_x][min_y]] -= 1
        board[min_x][min_y] = 0
        row, col = min_x, min_y
        return dist
    return 0


def checkBfs():
    for i in range(1, 7):
        if fish[i] != 0 and size > i:
            return True
    return False


while checkBfs():
    r = bfs(row, col)
    if r == 0:
        break
    answer += r
    if eat == size:
        size += 1
        eat = 0

print(answer)
