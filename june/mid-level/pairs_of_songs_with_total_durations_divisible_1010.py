########################################################################
#
#   @author:        yusuufaslan
#   @date:          03.06.2023
#   @problem:       1010. Pairs of Songs With Total Durations Divisible by 60
#
########################################################################


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result, counter = 0, [0] * 60
        
        for t in time:
            counter[t % 60] += 1

        for i in range (1, 30):
            result += counter[i] * counter[60 - i]
        
        return result + counter[0] * (counter[0]-1) // 2 + counter[30] * (counter[30]-1) // 2

"""
Problem Description:
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by
60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
"""