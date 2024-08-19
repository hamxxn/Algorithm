from itertools import combinations

n, m = map(int, input().split())
nums = map(int, input().split())
result = 0
for i in combinations(nums, 3):
    s = sum(i)
    if (s <= m) and (result < s):
        result = s
print(result)
