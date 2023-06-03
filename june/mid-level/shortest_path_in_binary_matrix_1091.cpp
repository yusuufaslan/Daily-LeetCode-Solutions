/*
    @author:        yusuufaslan
    @date:          01.06.2023
    @problem:       1091. Shortest Path in Binary Matrix
*/

class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int n = grid.size();

        if (grid[0][0] == 1 || grid[n-1][n-1] == 1)
            return -1;

        grid[0][0] = 1;
        queue<pair<int, int>> q;
        q.push({0, 0});

        int path_size = 0;

        while (!q.empty()) {
            int q_size = q.size();
            path_size++;

            while(q_size--) {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();

                if (x == n-1 && y == n-1)
                    return path_size;

                // right, left, up, down, bottom-right, top-right, bottom-left, top-left
                int direction_x[8] = {1, -1, 0, 0, 1, 1, -1, -1};
                int direction_y[8] = {0, 0, 1, -1, 1, -1, 1, -1};

                for (int i = 0; i < 8; i++) {
                    int new_x = x + direction_x[i];
                    int new_y = y + direction_y[i];
                    
                    if (new_x >= 0 && new_y >= 0 && new_x < n && new_y < n 
                            && grid[new_x][new_y] == 0) {
                        
                        grid[new_x][new_y] = 1;
                        q.push({new_x, new_y});
                    }
                }
            }
        }

        return -1;
    }
};


/*
Problem Definition:
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
*/