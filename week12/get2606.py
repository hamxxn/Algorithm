import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

visited = []

graph = [[] for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start):
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])


dfs(1)
answer = len(visited)
print(answer - 1)
