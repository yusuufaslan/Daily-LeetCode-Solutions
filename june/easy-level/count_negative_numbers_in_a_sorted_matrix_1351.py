########################################################################
#
#   @author:        yusuufaslan
#   @date:          08.06.2023
#   @problem:       1351. Count Negative Numbers in a Sorted Matrix
#
########################################################################


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int: 
        n, m = len(grid), len(grid[0])
        result =  0

        r, c = n - 1, 0

        while r >= 0 and c < m:
            if grid[r][c] < 0:
                result += m - c
                r -= 1
            else:
                c += 1

        return result 

"""
Problem Description:
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, 
return the number of negative numbers in grid.
"""