n, s = map(int, input().split())
num = list(map(int, input().split()))
answer = 0


def backtrack(startIdx):
    global answer
    if sum(l) == s and len(l) > 0:
        answer += 1

    for i in range(startIdx, n):
        l.append(num[i])
        backtrack(i + 1)
        l.pop()


l = []
backtrack(0)
print(answer)
