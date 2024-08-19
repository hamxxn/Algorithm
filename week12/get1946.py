import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
t = int(input())
answer = []
for j in range(t):
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: (x[0], x[1]))
    result = 1
    min_x = p[0][1]
    for i in range(1, n):
        if p[i][1] < min_x:
            result += 1
            min_x = p[i][1]
    answer.append(result)
for i in range(t):
    print(answer[i])
