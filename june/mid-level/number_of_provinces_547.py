########################################################################
#
#   @author:        yusuufaslan
#   @date:          04.06.2023
#   @problem:       547. Number of Provinces
#
########################################################################


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        numOfProvinces = 0
        visited = [False] * n


        def depthFirstSearch(node):
            visited[node] = True

            for neighbour in range(n):
                if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                   depthFirstSearch(neighbour) 

        for i in range(n):
            if not visited[i]:
                numOfProvinces += 1
                depthFirstSearch(i)

        return numOfProvinces

"""
Problem Description:
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""