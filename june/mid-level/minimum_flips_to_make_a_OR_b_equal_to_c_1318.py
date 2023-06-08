########################################################################
#
#   @author:        yusuufaslan
#   @date:          07.06.2023
#   @problem:       1318. Minimum Flips to Make a OR b Equal to c
#
########################################################################


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        result = 0

        while a or b or c:
            x1 = a & 1
            x2 = b & 1  
            x3 = c & 1  

            if x1 | x2 != x3:
                if x1 & x2:
                    result += 2
                else:
                    result += 1
            
            a = a >> 1
            b = b >> 1
            c = c >> 1

        return result

"""
Problem Description:
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits 
of a and b to make ( a OR b == c ). (bitwise OR operation).

Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 i
n their binary representation.
"""