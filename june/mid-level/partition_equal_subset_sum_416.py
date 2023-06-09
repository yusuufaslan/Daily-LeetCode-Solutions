########################################################################
#
#   @author:        yusuufaslan
#   @date:          09.06.2023
#   @problem:       416. Partition Equal Subset Sum
#
########################################################################


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        if totalSum % 2 != 0:
            return False
        
        targetSum = totalSum // 2

        dp = [False] * (targetSum + 1)

        dp[0] = True

        for num in nums:
            for j in range(targetSum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[targetSum]

"""
Problem Description:

Given an integer array nums, return true if you can partition the array into two 
subsets such that the sum of the elements in both subsets is equal or false otherwise.

"""