array = [
    [10,7,6,2],
    [9,8,7,6],
    [8,3,1,7],
    [1,1,1,8]
]

zeros = [[0 for i in range(len(array[0]))] for j in range(len(array))]

def snake(grid, zeros):
    global maxCol, maxRow
    lengthMax = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if ( x > 0 and abs(array[x-1][y] - array[x][y]) == 1 ):
                zeros[x][y] = max(zeros[x][y], zeros[x-1][y] + 1)
                if (lengthMax < zeros[x][y]):
                    lengthMax = zeros[x][y]
                    maxCol = y
                    maxRow = x
                
            
            if ( y > 0 and abs(array[x][y-1] - array[x][y]) == 1 ):
                zeros[x][y] = max(zeros[x][y], zeros[x][y-1] + 1)
                if (lengthMax < zeros[x][y]):
                    lengthMax = zeros[x][y]
                    maxCol = y
                    maxRow = x
    
    
    for z in zeros:
        print(z)


def getPath(grid, zeros, x, y):
    path = []
    pt = [x,y]
    path.append(pt)

    while (grid[x][y] != 0):
        if (x > 0 and grid[x][y] - 1 == grid[x -1][y]):
            pt = [x -1, y]
            path.append(pt)
            x -= 1
        if (y > 0 and grid[x][y] - 1 == grid[x ][y-1]):
            pt = [x, y-1]
            path.append(pt)
            y -= 1

    return path
