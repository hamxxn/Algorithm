import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

n = int(input())
board = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for i in range(n - 1):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

answer[1] = 1


def bfs(parent):
    for i in board[parent]:
        if answer[i] == 0:
            answer[i] = parent
            bfs(i)


bfs(1)

for i in range(2, n + 1):
    print(answer[i])
