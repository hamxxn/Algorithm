from collections import deque

v = int(input())
getTree = [[] for _ in range(v + 1)]
getNum = [[] for _ in range(v + 1)]
for i in range(v):
    l = list(map(int, input().split()))
    idx = l.pop(0)
    for i in range(int(len(l) / 2)):
        idx2 = l.pop(0)
        num = l.pop(0)
        getTree[idx].append(idx2)
        getNum[idx].append(num)
answer = 0


def bfs(parent, total, number):
    queue = deque()
    queue.append(parent)
    while queue:
        p = queue.popleft()
        # ㅣ스트에 저장되지 않은 숫자라면 append해주고 리스트에 추가


for i in range(len(getTree[1])):
    total = getNum[1][i]
    number = [1, getTree[i]]
    bfs(getTree[i], total, number)
