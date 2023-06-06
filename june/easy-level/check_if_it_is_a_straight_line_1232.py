########################################################################
#
#   @author:        yusuufaslan
#   @date:          05.06.2023
#   @problem:       1232. Check If It Is a Straight Line
#
########################################################################


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]

            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
                return False
        
        return True


"""
Problem Description:
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents 
the coordinate of a point. Check if these points make a straight line in the XY plane.
"""