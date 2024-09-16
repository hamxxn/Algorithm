n = int(input())
p = list(map(int, input().split()))
a = 0

p.sort()

for i in range(n):
    a += +p[i]
    p[i] = a

print(sum(p))
