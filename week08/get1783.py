n, m = map(int, input().split())
if n < 2 or m < 2:
    print(1)
elif n < 3:
    if m <= 2:
        print(1)
    elif m <= 4:
        print(2)
    elif m <= 6:
        print(3)
    else:
        print(4)
else:
    if m < 5:
        print(m)
    elif m < 7:
        print(4)
    else:
        print(m - 2)
