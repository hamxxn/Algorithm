def backtrack(cipher):
    vowel, consonant = 0, 0
    if len(cipher) == L:
        for c in cipher:
            if c in e:
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2:
            print("".join(cipher))

    for i in range(len(cipher), C):
        if cipher[-1] < ciNum[i]:
            cipher.append(ciNum[i])
            backtrack(cipher)
            cipher.pop()


L, C = map(int, input().split())
ciNum = list(map(str, input().split()))
e = ["a", "e", "i", "o", "u"]
ciNum.sort()

cipher = []

for i in range(0, len(ciNum) - L + 1):
    cipher.append(ciNum[i])
    backtrack(cipher)
    cipher.pop()
