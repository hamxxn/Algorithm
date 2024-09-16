n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
x, y = [], []
for i in range(n):
    if num[i] < 0:
        x.append(num[i])
    else:
        y.append(num[i])
idx = 0
answer = 0

while idx < len(x):
    answer += abs(x[idx]) * 2
    idx += m
idx = len(y) - 1

while idx >= 0:
    answer += y[idx] * 2
    idx -= m

if len(x) == 0 or len(y) == 0:
    if len(y) == 0:
        answer -= abs(x[0])
    else:
        answer -= y[len(y) - 1]
else:
    if abs(x[0]) >= y[len(y) - 1]:
        answer -= abs(x[0])
    else:
        answer -= y[len(y) - 1]
print(answer)
