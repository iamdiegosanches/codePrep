def solution(grid):
    # Chech row
    for row in range(9):
        numbers = list(filter(lambda x: x.isdigit(), grid[row]))
        if len(set(numbers)) != len(numbers):
            return False
    
    # Check for column
    for col in range(9):
        numbers = [grid[row][col] for row in range(9) if grid[row][col].isdigit()]
        if len(set(numbers)) != len(numbers):
            return False
                
    # Check sub-grids
    for i in range(3):
        for j in range(3):
            subgrid_numbers = []
            for row in range(i*3, (i+1)*3):
                for col in range(j*3, (j+1)*3):
                    if grid[row][col].isdigit():
                        subgrid_numbers.append(grid[row][col])
            if len(set(subgrid_numbers)) != len(subgrid_numbers):
                return False
    
    # Passed all the checks
    return True
    
