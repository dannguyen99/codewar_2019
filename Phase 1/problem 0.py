def isTwoSameSequences(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i:]):
            return True
    return False