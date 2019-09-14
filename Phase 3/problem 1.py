from math import factorial


def findTrailingZeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return int(count)

def numberOfZeroDigits(n):
    result = 0
    for i in range(n, 1, -1):
        plus = findTrailingZeros(i)
        if plus == 0:
            break
        else:
            result += plus
    return result


print(findTrailingZeros(10**8))
