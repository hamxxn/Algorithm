import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

r, c = map(int, input().split())
board = []

for i in range(r):
    board.append(list(input()))

di = [[1, 0], [-1, 0], [0, 1], [0, -1]]

letter = set(board[0][0])

max_answer = 0


def dfs(row, col, answer):
    global max_answer
    max_answer = max(answer, max_answer)

    for i in range(4):
        dx, dy = di[i][0] + row, di[i][1] + col
        if 0 <= dx < r and 0 <= dy < c:
            # 알파벳 확인
            if board[dx][dy] not in letter:
                letter.add(board[dx][dy])
                dfs(dx, dy, answer + 1)
                letter.remove(board[dx][dy])


dfs(0, 0, 1)
print(max_answer)
