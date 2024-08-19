n = input()
if "0" in n:
    for i in range(len(n)):
        sum += n[i]
    if sum % 3 == 0:
        n = sorted(n, reverse=True)
        print("".join(n))
    else:
        print(-1)
else:
    print(-1)
