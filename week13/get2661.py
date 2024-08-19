n = int(input())
num = [1]


def check():
    # 자를 개수
    for i in range(1, len(num)):
        if len(num) - i * 2 < 0:
            return True
        x = num[len(num) - i : len(num)]
        y = num[len(num) - i * 2 : len(num) - i]
        if x == y:
            return False
    return True


def backtrack(idx):
    if len(num) == n:
        for i in range(n):
            print(num[i], end="")
        exit(0)
    for i in range(1, 4):
        if idx == i:
            continue
        num.append(i)
        if check():
            backtrack(i)
        num.pop()


backtrack(1)
