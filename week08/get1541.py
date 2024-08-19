import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000000)
st = input().split()

str = st[0].split("-")

result = 0
for i in range(len(str)):
    answer = 0
    add = str[i].split("+")
    for j in range(len(add)):
        answer += int(add[j])
    if i != 0:
        result -= answer
    else:
        result += answer
print(result)
