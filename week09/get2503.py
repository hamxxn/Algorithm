from itertools import permutations

n = int(input())

num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(n):
    check, strike, ball = map(int, input().split())
    check = list(map(int, str(check)))
    remove = 0
    for i in range(len(num)):
        s = 0
        b = 0
        i -= remove
        for j in range(3):
            if num[i][j] == check[j]:
                s += 1
            elif check[j] in num[i]:
                b += 1
        if (strike != s) or (ball != b):
            num.remove(num[i])
            remove += 1
print(len(num))
