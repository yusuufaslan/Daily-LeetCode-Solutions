########################################################################
#
#   @author:        yusuufaslan
#   @date:          07.06.2023
#   @problem:       2527. Find Xor-Beauty of Array
#
########################################################################


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            result = result ^ nums[i]

        return result

"""
The key observation is that the triplets ((nums[i] | nums[j]) & nums[k]) occurs in pairs except when i=j=ki=j=ki=j=k.

when i=j=ki = j = ki=j=k, the result ((nums[i] | nums[j]) & nums[k]) is the the number itself.
when i=ji = ji=j but i≠ki \neq ki=k, we would have nums[i] & nums[k] and nums[k] & nums[i] be valid triplets for each pair of number in nums. XORing them would give 0.
otherwise, for each nums[k], ((nums[i] | nums[j]) & nums[k]) and ((nums[j] | nums[i]) & nums[k]) would both be a valid triplets and be considered in the final result. Obviously they are the same and XORing them in the last step would make them 0.
Hence, the result is just the XOR of all numbers in the array.
"""



"""
Problem Description:
You are given a 0-indexed integer array nums.

The effective value of three indices i, j, and k is defined 
as ((nums[i] | nums[j]) & nums[k]).

The xor-beauty of the array is the XORing of the effective 
values of all the possible triplets of indices (i, j, k) where 0 <= i, j, k < n.

Return the xor-beauty of nums.

Note that:

val1 | val2 is bitwise OR of val1 and val2.
val1 & val2 is bitwise AND of val1 and val2.
"""