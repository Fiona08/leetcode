#63


# Time:  O(m * n) m: rows,n columns
# Space: O(n)


# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.


class DynamicProgrammingSol():
    def uniquePathII(self,obstacle_grid):
        rows,cols=len(obstacle_grid),len(obstacle_grid[0])
        number_of_path=[0]*cols
        number_of_path[0]=1
        for row in range(rows):
            if obstacle_grid[row][0]==1:
                number_of_path[0]=0
            for col in range(1,cols):
                if obstacle_grid[row][col]==1:
                    number_of_path[col]=0
                else:
                    number_of_path[col]+=number_of_path[col-1]
        return  number_of_path[-1]        
