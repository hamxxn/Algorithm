num = []
for i in range(0, 10001):
    num.append([True, i])

for i in range(1, 10001):
    if i < 10:
        if num[2 * i][0]:
            num[2 * i][0] = False
    else:
        s = 0
        x = i
        y = 0
        while x != 0:
            y = x % 10
            s += y
            x //= 10
        s += i
        if s < 10001 and num[s][0]:
            num[s][0] = False


for i in range(1, len(num)):
    if num[i][0]:
        print(num[i][1])
