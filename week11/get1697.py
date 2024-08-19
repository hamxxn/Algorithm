from collections import deque

n, k = map(int, input().split())

board = [0] * (100001)

board[n] = 1

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k:
        print(board[x] - 1)
        break

    for i in [x + 1, x - 1, 2 * x]:
        if 0 <= i <= 100000 and board[i] == 0:
            board[i] = board[x] + 1
            queue.append(i)
