def groupingDishes(dishes):
    dict = {}
    for dish in dishes:
        main_dish = dish[0]
        dish = dish[1:]
        for i, v in enumerate(dish):
            if v in dict:
                dict[v] = dict[v] + [main_dish]
            else:
                dict[v] = [main_dish]
                
    dict = { k:list(set(v)) for k, v in dict.items() if len(v) > 1 and k != v}
    
    new = sorted(dict.items())
    dictlist = []
    for i in new:
        dictlist.append([i[0],*sorted(i[1])])
        
    return dictlist
    
    
