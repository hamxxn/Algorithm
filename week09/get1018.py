n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input()))


def check(startrow, startcol, color):
    answer = 0
    for i in range(startrow, startrow + 8):
        for j in range(startcol, startcol + 8):
            if board[i][j] == color:
                if (i + j) % 2 != 0:
                    answer += 1
            elif board[i][j] != color:
                if (i + j) % 2 == 0:
                    answer += 1
    return answer


result = 8 * 8
for i in range(n - 7):
    for j in range(m - 7):
        if board[i][j] == "B":
            result = min(check(i, j, "W"), check(i, j, "B"), result)
        else:
            result = min(check(i, j, "W"), check(i, j, "B"), result)
print(result)
