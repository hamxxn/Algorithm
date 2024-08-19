import math
import sys

input = sys.stdin.readline
n = int(input())
result = 0
prime = []
arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n) + 1)):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1


for i in range(2, n + 1):
    if arr[i]:
        prime.append(i)
start = 0
end = 0
s = 0
while end <= len(prime):
    s = sum(prime[start:end])
    if s == n:
        result += 1
        end += 1
    elif s < n:
        end += 1
    elif s > n:
        start += 1
print(result)
