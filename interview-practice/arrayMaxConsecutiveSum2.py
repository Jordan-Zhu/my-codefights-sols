def arrayMaxConsecutiveSum2(inputArray):
    max_val = 0
    max_curr = inputArray[0]
    
    for e in inputArray:
        max_val += e
        if max_val < e:
            max_val = e
        if max_val > max_curr:
            max_curr = max_val 
    
    return max_curr
