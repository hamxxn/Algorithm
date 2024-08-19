l, c = map(int, input().split())
word = list(map(str, input().split()))
word.sort()
vowel = ["a", "e", "i", "o", "u"]


def checkVowel(str, check, plus):
    if plus:
        if str in vowel:
            check[0] += 1
        else:
            check[1] += 1
    else:
        if str in vowel:
            check[0] -= 1
        else:
            check[1] -= 1
    return check


def backtrack(words, idx, check):
    if len(words) == l:
        if check[0] >= 1 and check[1] >= 2:
            for i in range(l):
                print(words[i], end="")
            print()
        return
    for i in range(idx, len(word)):
        check = checkVowel(word[i], check, True)
        words.append(word[i])
        backtrack(words, i + 1, check)
        check = checkVowel(word[i], check, False)
        words.pop()


for i in range(0, c - l + 1):
    check = [0, 0]
    check = checkVowel(word[i], check, True)
    backtrack([word[i]], i + 1, check)
