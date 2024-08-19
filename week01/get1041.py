n = int(input())
num = list(map(int, input().split()))
if n == 1:
    num.sort()
    print(sum(num[:5]))
else:
    # 1면
    one = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    one *= min(num)
    # 2면
    minN = []
    minN.append(min(num[0], num[5]))
    minN.append(min(num[1], num[4]))
    minN.append(min(num[2], num[3]))
    minN.sort()
    s = minN[0] + minN[1]
    two = (n - 2) * 4 + (n - 1) * 4
    two *= s
    # 3면
    s = minN[0] + minN[1] + minN[2]
    three = s * 4

    print(one + two + three)
