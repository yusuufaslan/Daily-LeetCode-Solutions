########################################################################
#
#   @author:        yusuufaslan
#   @date:          10.06.2023
#   @problem:       1802. Maximum Value at a Given Index in a Bounded Array
#
########################################################################


class Solution:
    def check(self, a):
        left_offset = max(a - self.index, 0)
        result = (a + left_offset) * (a - left_offset + 1) // 2
        
        right_offset = max(a - ((self.n - 1) - self.index), 0)
        result += (a + right_offset) * (a - right_offset + 1) // 2

        return result - a
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        self.n = n
        self.index = index

        maxSum -= n
        left, right = 0, maxSum

        while left < right:
            mid = (left+ right + 1) // 2

            if self.check(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1  

        result = left + 1

        return result

"""
Problem Description:

You are given three positive integers: n, index, and maxSum. You want to construct an array
nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.
"""