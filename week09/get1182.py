from itertools import combinations

n, s = map(int, input().split())

num = list(map(int, input().split()))
answer = 0
for i in range(1, n + 1):
    combi = list(combinations(num, i))
    for j in range(0, len(combi)):
        combisum = sum(combi[j])
        if s == combisum:
            answer += 1
print(answer)
