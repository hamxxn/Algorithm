import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
t = int(input())
for i in range(t):
    n = int(input())
    people = []
    for j in range(n):
        people.append(list(map(int, input().split())))
    people.sort(key=lambda x: (x[0], x[1]))
    top = people[0][1]
    count = 1
    for z in range(1, n):
        if people[z][1] < top:
            count += 1
            top = people[z][1]
    print(count)
