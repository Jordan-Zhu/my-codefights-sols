def rotateImage(a):
    if len(a) == 1:
        return a
    
    rotated = []
    for i in range(len(a)):
        temp = []
        for j in range(len(a)):
            temp.append(a[j][i])
        rotated.append(list(reversed(temp)))
    
    return rotated
