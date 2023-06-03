########################################################################
#
#   @author:        yusuufaslan
#   @date:          03.06.2023
#   @problem:       1376. Time Needed to Inform All Employees
#
########################################################################


class Solution:
    def depthFirstSearch(self, manager, informTime, adjacencyList):
        maxTime = 0
        
        for subordinate in adjacencyList[manager]:
            maxTime = max(maxTime, self.depthFirstSearch(subordinate, informTime, adjacencyList))
        
        return maxTime + informTime[manager]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacencyList = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                adjacencyList[manager[i]].append(i)
        
        return self.depthFirstSearch(headID, informTime, adjacencyList)
    
"""
Problem Description:
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. 
Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, 
and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, 
all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
"""
