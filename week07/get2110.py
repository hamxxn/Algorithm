import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
n, c = map(int, input().split())
home = []
for i in range(n):
    home.append(int(input()))
home.sort()

if c == 2:
    print(home[n - 1] - home[0])
else:
    low, high = 1, home[n - 1] - home[0]
    answer = 0
    while low <= high:
        mid = (high + low) // 2
        # 0번 집에 설치
        count = 1
        compare = home[0]
        # 설치 시작
        for i in range(1, n):
            # 설치
            if home[i] - compare >= mid:
                compare = home[i]
                count += 1
        if count >= c:
            low += 1
            answer = mid
        else:
            high -= 1
    print(answer)
