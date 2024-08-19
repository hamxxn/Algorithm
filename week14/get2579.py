n = int(input())
num = [0]
for i in range(n):
    num.append(int(input()))
count = [0] * (n + 1)

if len(num) <= 3:
    print(sum(num))
else:
    count[1] = num[1]
    count[2] = num[1] + num[2]
    for i in range(3, n + 1):
        # 3번째 칸부터는  1칸 올라온 경로와
        # 2칸으로 올라온 경로
        # 추가 : 연속 3번은 불가하다.
        count[i] = max(count[i - 2] + num[i], count[i - 3] + num[i - 1] + num[i])
    print(count[n])
