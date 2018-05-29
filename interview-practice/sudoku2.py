def subgrid():
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return {key: None for key in keys}

def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def line_is_valid(row):
    tmp_dict = set()
    
    for i in range(len(row)):
        if row[i] != '.' and row[i] in tmp_dict:
            return False
        else:
            tmp_dict.add(row[i])
    
    return True

def check_grid(grid):
    valid = True
    for i in range(len(grid)):
        valid = line_is_valid(grid[i])
        if not valid:
            break
    
    return valid
            

def sudoku2(grid):
    rows_valid = check_grid(grid)
    cols_valid = check_grid(list(zip(*reversed(grid))))
    
    sub_grid_valid = True
    for i in range(0, len(grid), 3):
        if not sub_grid_valid:
            break
            
        sub_mat = grid[i:i+3]
        
        for j in range(0, len(grid), 3):
            tmp_list = [x[j:j+3] for x in sub_mat]
            tmp_list = [tmp_list[k][l] for k in range(len(tmp_list)) for l in range(len(tmp_list[k]))]
            
            sub_grid_valid = line_is_valid(tmp_list)
            
            if not sub_grid_valid:
                break
                
    return cols_valid and rows_valid and sub_grid_valid

    
    
            