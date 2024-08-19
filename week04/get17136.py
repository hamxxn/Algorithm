board = []
for i in range(10):
    board.append(list(map(int, input().split())))
total = [0] * 5


def checkIs1(row, col, count):
    # 네모
    for i in range(row, row + 2):
        for j in range(col, col + 2):
            if row == i and col == j:
                continue
            if board[i][j] != 1:
                return False
    # count
    x, y = row - 1, col - 1
    for i in range(count):
        if board[x][col + 1] != 1:
            return False
        x = -1
        if board[row + 1][y] != 1:
            return False
        y -= 1
    print(row)
    print(col)
    print("통과")
    return True


def backtrack(row, col, count, idx):
    # 모두 1일시
    if checkIs1(row, col, count):
        # 박스 0으로 바꾸기
        for i in range(row, row + 2):
            for j in range(col, col + 2):
                board[i][j] = 0
        # count 0으로 바꾸기
        x, y = row - 1, col - 1
        for i in range(count):
            board[x][col + 1] = 0
            x = -1
            board[row + 1][y] = 0
            y -= 1

        total[idx] += 1
        total[idx - 1] -= (idx) * (idx)
        if idx < 5:
            backtrack(row + 1, col + 1, count + 1, idx + 1)


for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            total[0] += 1
            board[i][j] = 0
            backtrack(i, j, 0, 1)

for i in range(5):
    print(total[i])
