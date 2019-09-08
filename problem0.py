def sumOfAllDigitsInRange(l, r):
    sum = 0
    for i in range(l, r+1):
        digits = [int(d) for d in str(i)]
        for j in digits:
            sum += j
    return sum