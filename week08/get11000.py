n = int(input())
lecture = []
for i in range(n):
    l = list(map(int, input().split()))
    lecture.append(l)
lecture.sort(key=lambda x: (x[0], x[1]))

finish = []
finish.append(lecture[0][1])
for i in range(1, n):
    is_in = False
    for j in range(len(finish)):
        if finish[j] <= lecture[i][0]:
            finish[j] = lecture[i][1]
            is_in = True
            break
    if not is_in:
        finish.append(lecture[i][1])

print(len(finish))
