n = int(input())
mynum = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
mynum.sort()


def binarysearch(lowidx, highidx, key):
    global check
    mididx = lowidx + (highidx - lowidx) // 2
    if lowidx > highidx:
        return
    if key == mynum[mididx]:
        print(1, end=" ")
        check += 1
    elif key > mynum[mididx]:
        binarysearch(mididx + 1, highidx, key)
    elif key < mynum[mididx]:
        binarysearch(lowidx, mididx - 1, key)


for i in range(m):
    check = 0
    binarysearch(0, n - 1, num[i])
    if check == 0:
        print(0, end=" ")
