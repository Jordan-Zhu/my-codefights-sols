def firstNotRepeatingCharacter(s):
    buckets = [0] * 26
    
    for c in s:
        buckets[ord(c) - 97] += 1
        
    for i in s:
        if buckets[ord(i) - 97] == 1:
            # print(i)
            return i
    return "_"
