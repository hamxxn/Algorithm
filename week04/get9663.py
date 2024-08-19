import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

n = int(input())
col = []
total = 0


def back(idx):
    global total
    if len(col) == n:
        total += 1
        return
    for i in range(n):
        if checkUp(idx, i) and (not i in col):
            col.append(i)
            back(idx + 1)
            col.pop()


def checkUp(idx, pC):
    check = True
    right, left = pC, pC
    for i in range(idx, -1, -1):
        left -= 1
        right += 1
        if (col[i] == left) or (col[i] == right):
            check = False
            return check
    return check


for i in range(n):
    col.append(i)
    back(0)
    col.pop()
print(total)
