def sumInRange(nums, queries):
    dic = {}
    cache_sum = 0
    
    for i, e in enumerate(nums):
        cache_sum += e
        dic["0_{}".format(i)] = cache_sum
        
    sum_r = 0
    for x in queries:
        a, b  = x
        if '{}_{}'.format(a,b) in dic:
            sum_r += dic['{}_{}'.format(a,b)]
        else:
            t = dic['0_{}'.format(b)] - dic['0_{}'.format(a-1)]
            # dic['{}_{}'.format(a,b)] = t
            sum_r += t
            
        
    return sum_r % 1000000007
