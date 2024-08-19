import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
m = int(input())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
visited[1] = True
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1

answer = 0


def dfs(row):
    global answer
    visited[row] = True
    answer += 1
    for i in range(0, len(arr[row])):
        if arr[row][i] == 1 and visited[i] == False:
            dfs(i)


for i in range(1, n + 1):
    if arr[1][i] == 1 and visited[i] == False:
        dfs(i)
print(answer)
