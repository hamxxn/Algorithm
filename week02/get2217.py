n = int(input())
k = []
for i in range(n):
    k.append(int(input()))
answer = 0
k.sort()
for i in range(0, n):
    answer = max(answer, k[i] * (n - i))
print(answer)
