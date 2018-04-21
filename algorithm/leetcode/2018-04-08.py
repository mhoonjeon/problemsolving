# 463. Island Perimeter


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    width = len(grid[0])
    height = len(grid)

    # create greater grid with extra row and column surrounding original grid
    outer_grid = [[0 for x in range(width+2)] for y in range(height+2)]

    # copy original grid to outer_grid
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                outer_grid[i+1][j+1] = grid[i][j]

    # count 1's with number of surround 1's
    stripe_num = 0
    for i in range(1, len(outer_grid)):
        for j in range(1, len(outer_grid[0])):
            if outer_grid[i][j] == 1:
                stripe_per_cell = 4
                if outer_grid[i+1][j] == 1:
                    stripe_per_cell -= 1
                if outer_grid[i-1][j] == 1:
                    stripe_per_cell -= 1
                if outer_grid[i][j+1] == 1:
                    stripe_per_cell -= 1
                if outer_grid[i][j-1] == 1:
                    stripe_per_cell -= 1
                stripe_num += stripe_per_cell

    return stripe_num


""" http://liqichen.com/daily-leetcode-463-island-perimeter/
더 빠르다. 일단 내 코드는 같은 셀을 여러번 계산하는데 아래 코드는 그렇지 않는다.

def islandPerimeter(self, grid):
    sides = 0
    for i in range(len(grid)):
        prev = 0
        for t in grid[i]:
            if t!=prev:
                prev = t
                sides+=1
        if grid[i][len(grid[i])-1]==1:
            sides+=1

    for i in range(len(grid[0])):
        prev = 0
        for t in range(len(grid)):
            if grid[t][i]!=prev:
                prev = grid[t][i]
                sides+=1
        if grid[len(grid)-1][i]==1:
            sides+=1

    return sides
"""


# 766. Toeplitz Matrix

def isToeplitzMatrix(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            try:
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
            except:
                pass
    return True


""" https://leetcode.com/problems/toeplitz-matrix/discuss/113385/Python-Easy-and-Concise-Solution

except보다range를 row, col 모두 한 줄 덜 확인하면 된다.

def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True
"""
