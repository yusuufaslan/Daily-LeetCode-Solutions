########################################################################
#
#   @author:        yusuufaslan
#   @date:          03.06.2023
#   @problem:       1338. Reduce Array Size to The Half
#
########################################################################


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        frequencies = list(counts.values())
        frequencies.sort()


        min_set_size, removed, half = 0, 0, len(arr) // 2

        while removed < half:
            min_set_size += 1
            removed += frequencies.pop()

        return min_set_size
    
"""
Problem Description:
You are given an integer array arr. You can choose a set of integers 
and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers 
of the array are removed.
"""