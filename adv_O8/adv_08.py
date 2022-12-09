def count_visible(grid):
    score = 0
    for line in grid:
        for cell in line:
            if cell[1] == 1:
                print(1, end='')
                score+=1
            else:
                print(0, end='')
        print()
    return score

def get_visible(grid):
    len_line = len(grid[0])
    len_grid = len(grid)
    i = 0
    while i < len_grid:
        j = 0
        tallest = -1
        while j < len_line:
            if (int)(grid[i][j][0]) > tallest:
                tallest = (int)(grid[i][j][0])
                grid[i][j][1] = 1
            j+=1
        i+=1
    i = 0
    while i < len_grid:
        j = 0
        tallest = -1
        while j < len_line:
            if (int)(grid[i][len_line - j - 1][0]) > tallest:
                tallest = (int)(grid[i][len_line - j - 1][0])
                grid[i][len_line - j - 1][1] = 1
            j+=1
        i+=1
    i = 0
    while i < len_line:
        j = 0
        tallest = -1
        while j < len_grid:
            if (int)(grid[j][i][0]) > tallest:
                tallest = (int)(grid[j][i][0])
                grid[j][i][1] = 1
            j+=1
        i+=1
    i = 0
    while i < len_line:
        j = 0
        tallest = -1
        while j < len_grid:
            if (int)(grid[len_grid - j - 1][i][0]) > tallest:
                tallest = (int)(grid[len_grid - j - 1][i][0])
                grid[len_grid - j -1][i][1] = 1
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
    score = get_visible(grid)
    print(score)
