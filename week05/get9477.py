import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)


def dfs(idx, count):
    cycle_l.append(idx)
    visit[idx] = True
    if visit[st[idx]]:
        if st[idx] in cycle_l:
            count += cycle_l[cycle_l.index(st[idx]) :]
        return
    dfs(st[idx], count)


for i in range(int(input())):
    n = int(input())
    count = []
    st = [0] + list(map(int, input().split()))
    visit = [False for _ in range(n + 1)]

    for i in range(1, n + 1):
        if not visit[i]:
            cycle_l = []
            dfs(i, count)
    print(n - len(count))
