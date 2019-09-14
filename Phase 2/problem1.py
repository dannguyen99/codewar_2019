def oddNumbers(s):
    choices = 1
    possible = 9
    used = []
    for i in range(len(s)):
        if i == 0:
            choices *= 5
        elif s[-i -1] in used:
            choices *= 1
        else:
            choices *= possible
            possible -= 1
        used.append(s[-i -1])
    return choices


print(oddNumbers("bbbbbbbbbbbbbbbccccccbbbbbbeeezzzxxx"))
