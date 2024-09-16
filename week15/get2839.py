n = int(input())
five = n // 5
left = n % 5

while five >= 0:
    if left % 3 == 0:
        three = left // 3
        print(five + three)
        break
    five -= 1
    left += 5
else:
    print(-1)
