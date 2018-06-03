def areFollowingPatterns(strings, patterns):
    dict = {}
    
    for i in range(len(patterns)):
        if patterns[i] in dict:
            if dict[patterns[i]] != strings[i]:
                return False
        else:
            if strings[i] in dict.values():
                return False
            dict[patterns[i]] = strings[i]
                
    return True