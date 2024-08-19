k, n = map(int, input().split())
r = []
for i in range(k):
    r.append(int(input()))


def binarysearch(low, high):
    global mid
    mid = low + (high - low) // 2
    if low > high:
        return
    count = 0
    for i in range(k):
        count += r[i] // mid
    if count < n:
        binarysearch(low, mid - 1)
    elif count >= n:
        binarysearch(mid + 1, high)


binarysearch(1, max(r))

print(mid)
