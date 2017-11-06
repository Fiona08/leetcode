#64


# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right 
# which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.


class DynamicProgrammingSol():
    # Time:  O(m * n)
    # Space: O(m + n)
    def minPathSum1(self,grid):
        path_sum=grid[0]
        for row in range(len(grid)):
            if row==0:
                for col in range(1,len(grid[0])):
                    path_sum[col]+=path_sum[col-1]
            else:
                for col in range(len(grid[0])):
                    if col==0:
                        path_sum[col]+=grid[row][col]
                    else:
                        path_sum[col]=min(path_sum[col],path_sum[col-1])+grid[row][col]
        return path_sum[-1]


    # Time:  O(m * n)
    # Space: O(m + n)
    def minPathSum2(self,grid):
        path_sum=grid[0]
        for col in range(1,len(grid[0])):
            path_sum[col]+=path_sum[col-1]
        for row in range(1,len(grid)):
            path_sum[0]+=grid[row][0]
            for col in range(1,len(grid[0])):
                path_sum[col]=min(path_sum[col],path_sum[col-1])+grid[row][col]
        return path_sum[-1]
