n = int(input())
le = []
for i in range(n):
    le.append(list(map(int, input().split())))
le.sort(key=lambda x: (x[1], x[0]))
answer = 0
finish = le[0][1]
for i in range(1, n):
    if le[i][0] >= finish:
        answer += 1
        finish = le[i][1]
print(answer)
