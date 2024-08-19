import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)
n = int(input())
num = []
visited = [[False for _ in range(n)] for _ in range(n)]
result = []
for i in range(n):
    l = list(input())
    num.append(l)

di = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(x, y, answer):
    visited[x][y] = True
    answer += 1
    for i in range(4):
        dx = di[i][0] + x
        dy = di[i][1] + y
        if (
            0 <= dx < n
            and 0 <= dy < n
            and num[dx][dy] == "1"
            and visited[dx][dy] == False
        ):

            answer = dfs(dx, dy, answer)
    return answer


for i in range(n):
    for j in range(n):
        if num[i][j] == "1" and visited[i][j] == False:
            result.append(dfs(i, j, 0))


result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
