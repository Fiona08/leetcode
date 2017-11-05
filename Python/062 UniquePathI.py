#62

# Time:  O(m*n) m: rows, n:columns
# Space: O(n)


# A robot is located at the top-left corner of 
# a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid 
# (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?

class DynamicProgrammingSol():
    def uniquePathI(self,row,column):
        number_of_path=[1]*column
        for cur_row in range(1,row):
            for cur_col in range(1,column):
                number_of_path[cur_col]+=number_of_path[cur_col-1]
            print(number_of_path)
        return number_of_path[-1]
