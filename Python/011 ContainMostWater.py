#011
 
 
# Time:  O(n)
# Space: O(1)


# Given n non-negative integers a1, a2, ..., an, 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints 
# of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, 
# such that the container contains the most water.
# 
# Note: You may not slant the container.


class greedySol():
    def containMostWater(self,height):
        left_hei_idx,right_hei_idx,max_area=0,len(height)-1,0
        while left_hei_idx<right_hei_idx:
            max_area=max(max_area,min(height[left_hei_idx],height[right_hei_idx])*(right_hei_idx-left_hei_idx))
            if height[left_hei_idx] < height[right_hei_idx]:
                left_hei_idx+=1
            else:
                right_hei_idx-=1
        return max_area
