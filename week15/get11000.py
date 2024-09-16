import heapq
import sys

input = sys.stdin.readline
n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))
time.sort()
queue = []
heapq.heappush(queue, time[0][1])
for i in range(1, n):
    if queue[0] <= time[i][0]:
        r = heapq.heappop(queue)
    heapq.heappush(queue, time[i][1])
print(len(queue))
