n, m = map(int, input().split())
num = []
for i in range(1, n + 1):
    num.append(i)


def backtrack(num):
    for i in range(1, n + 1):
        if i not in num:
            num.append(i)
            if len(num) != m:
                backtrack(num)
            else:
                for j in num:
                    print(j, end=" ")
                print()
            num.pop()


backtrack([])
