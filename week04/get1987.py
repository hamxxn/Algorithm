r, c = map(int, input().split())
num = []
for i in range(r):
    num.append(list(input()))
getdi = set(num[0][0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
Max = 0


def backtrack(row, col, count):
    global Max
    Max = max(count, Max)
    for i in range(4):
        x, y = row + dx[i], col + dy[i]
        if 0 <= x < r and 0 <= y < c:
            if not num[x][y] in getdi:
                getdi.add(num[x][y])
                backtrack(x, y, count + 1)
                getdi.remove(num[x][y])


backtrack(0, 0, 1)
print(Max)
