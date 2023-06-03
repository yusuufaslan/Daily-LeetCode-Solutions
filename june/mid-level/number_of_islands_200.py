########################################################################
#
#   @author:        yusuufaslan
#   @date:          03.06.2023
#   @problem:       200. Number of Islands
#
########################################################################


class Solution:
    def depthFirstSearch(self, grid, i, j):
        n = len(grid)
        m = len(grid[0])

        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != '1':
            return

        grid[i][j] = '#'
        self.depthFirstSearch(grid, i + 1, j)
        self.depthFirstSearch(grid, i - 1, j) 
        self.depthFirstSearch(grid, i, j + 1) 
        self.depthFirstSearch(grid, i, j - 1) 


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        numOfIslands = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.depthFirstSearch(grid, i, j)
                    numOfIslands += 1

        return numOfIslands


"""
Problem Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""