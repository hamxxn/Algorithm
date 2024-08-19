n, m = map(int, input().split())
tree = list(map(int, input().split()))


def binarysearch(low, high):
    global mid
    mid = low + (high - low) // 2
    if low > high:
        return
    total = 0
    for i in range(n):
        if tree[i] - mid > 0:
            total += tree[i] - mid
    if total >= m:
        binarysearch(mid + 1, high)
    else:
        binarysearch(low, mid - 1)


binarysearch(0, max(tree))
print(mid)
