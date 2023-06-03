########################################################################
#
#   @author:        yusuufaslan
#   @date:          02.06.2023
#   @problem:       2101. Detonate the Maximum Bombs
#
########################################################################


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        max_bombs = 0
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2]**2 >= (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])** 2:
                    graph[i] += [j]

        def depthFirstSearch(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    depthFirstSearch(child, visited)
        
        for i in range(n):
            visited = set([i])
            depthFirstSearch(i, visited)
            max_bombs = max(max_bombs, len(visited))

        return max_bombs

"""
Problem Description:
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the 
shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the 
X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These 
bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
"""