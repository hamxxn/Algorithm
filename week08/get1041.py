n = int(input())
num = list(map(int, input().split()))
answer = 0
if n <= 1:
    for i in range(5):
        num.sort()
        answer += num[i]
else:
    m1 = min(num[0], num[5])
    m2 = min(num[1], num[4])
    m3 = min(num[2], num[3])
    one = min(m1, m2, m3)
    answer += one * (n - 2) * (5 * n - 6)
    two = min(m1 + m2, m1 + m3, m2 + m3)
    answer += two * 4 * (2 * n - 3)
    three = m1 + m2 + m3
    answer += three * 4
print(answer)
