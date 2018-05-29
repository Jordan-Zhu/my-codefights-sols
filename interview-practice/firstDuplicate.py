def firstDuplicate(a):
    for i in range(0, len(a)):
        val = abs(a[i])
        if a[val - 1] < 0:
            return abs(val)
        else:
            a[val - 1] = -a[val - 1]
    return -1