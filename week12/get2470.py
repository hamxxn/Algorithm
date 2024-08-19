n = int(input())

num = list(map(int, input().split()))
num.sort()

answer = [num[0], num[n - 1]]
min_0 = abs(num[0] + num[n - 1])
low = 0
high = n - 1
while low < high:
    m = num[low] + num[high]
    if min_0 > abs(m):
        min_0 = abs(m)
        answer[0] = num[low]
        answer[1] = num[high]
    if m == 0:
        break
    elif m < 0:
        low += 1
    elif m > 0:
        high -= 1
print(answer[0], answer[1])
