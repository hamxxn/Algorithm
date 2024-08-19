import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

s = list(input())
s.pop()
t = list(input())
t.pop()


def plusA(first, second):
    new_first = first[:]  # Create a copy of the list
    new_first.append("A")

    return Bfs(new_first, second)


def plusBreverse(first, second):
    new_first = first[:]  # Create a copy of the list
    new_first.append("B")

    new_first.reverse()
    return Bfs(new_first, second)


def Bfs(first, second):
    if len(first) == len(second):
        if first == second:
            return True
        return False

    return plusA(first, second) or plusBreverse(first, second)


if Bfs(s, t):
    print(1)
else:
    print(0)
