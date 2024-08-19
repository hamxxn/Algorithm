import heapq
import sys

input = sys.stdin.readline
n = int(input())
leture = []
for i in range(n):
    a, b = map(int, input().split())
    leture.append([a, b])
leture.sort(key=lambda x: (x[0], x[1]))

stack = [leture[0][1]]
print(leture)
for i in range(1, n):
    if stack[0] <= leture[i][0]:
        print(heapq.heappop(stack))
    heapq.heappush(stack, leture[i][1])
    print(stack)
print(len(stack))
