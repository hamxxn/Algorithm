import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
n = int(input())
card = list(map(int, input().split()))
maxIdx = card.index(max(card))
answer = 0
for i in range(maxIdx + 1, n):
    answer += card[maxIdx] + card[i]
for i in range(maxIdx - 1, -1, -1):
    answer += card[maxIdx] + card[i]
print(answer)
