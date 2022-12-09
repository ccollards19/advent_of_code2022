def count_visible(grid):
    score = 0
    for line in grid:
        for cell in line:
            print(cell[1], end=' ')
            if cell[1] > score:
                score = cell[1]
        print()
    return score;

def get_up(grid, i, j, size):
    up = 0
    i+=-1
    while i >= 0:
        up+=1
        if (int)(grid[i][j][0]) >= size:
            break
        i+=-1
    if up == 0:
        up = 1
    return up

def get_down(grid, i, j, size):
    down = 0
    i+=1
    while i < len(grid):
        down+=1
        if (int)(grid[i][j][0]) >= size:
            break
        i+=1
    if down == 0:
        down = 1
    return down

def get_left(grid, i, j, size):
    left = 0
    j+=-1
    while j >= 0:
        left+=1
        if (int)(grid[i][j][0]) >= size:
            break
        j+=-1
    if left == 0:
        left = 1
    return left

def get_right(grid, i, j, size):
    right = 0
    j+=1
    while j < len(grid[0]):
        right+=1
        if (int)(grid[i][j][0]) >= size:
            break
        j+=1
    if right == 0:
        right = 1
    return right
    
def get_score(grid, i, j):
    size = (int)(grid[i][j][0])
    up = get_up(grid, i, j, size)
    down = get_down(grid, i, j, size)
    left = get_left(grid, i, j, size)
    right = get_right(grid, i, j, size)
    print (up, down, left, right)
    return (up * down * left * right)
    

def get_view(grid):
    len_line = len(grid[0])
    len_grid = len(grid)
    i = 0
    while i < len_grid:
        j = 0
        while j < len_line:
            grid[i][j][1] = get_score(grid, i, j)
            j+=1
        i+=1
    return count_visible(grid)

grid = []
row = []
with open('input') as file:
    for line in file :
        line = line.strip('\n')
        for char in line:
            cell = [char, 0]
            row.append(cell)
        grid.append(row)
        row = []
    score = get_view(grid)
    print(score)
