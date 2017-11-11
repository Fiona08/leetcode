#55


# Time:  O(n)
# Space: O(1)


# Given an array of non-negative integers, 
# you are initially positioned at the first index of the array.
# Each element in the array represents 
# your maximum jump length at that position.
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.


class greedySol():
    def jumpGameI(self,steps):
        max_pos=0
        steps[-1]=float('-Inf')
        for idx, step in enumerate(steps):
            max_pos=max(max_pos,idx+step)
            if  max_pos >=len(steps)-1:
                return True
        return max_pos >= en(steps)-1
