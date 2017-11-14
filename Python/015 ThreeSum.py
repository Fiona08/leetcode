#15


# Time:  O(n^2)
# Space: O(1)


# Given an array S of n integers, are there elements a, b, c in S 
# such that a + b + c = 0? Find all unique triplets in the array 
# which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
# 
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class arraySol():
    def threeSum(self,nums):
        nums=sorted(nums)
        front_idx,threeNum_sum_0=0,[]
        while front_idx<len(nums)-2:
            if front_idx==0 or nums[front_idx]!=nums[front_idx-1]:
                mid_idx,end_idx=front_idx+1,len(nums)-1
                while mid_idx<end_idx:
                    if nums[front_idx]+nums[mid_idx]+nums[end_idx]<0:
                        mid_idx+=1 
                    elif nums[front_idx]+nums[mid_idx]+nums[end_idx]>0:
                        end_idx-=1
                    else:
                        threeNum_sum_0.append([nums[front_idx],nums[mid_idx],nums[end_idx]])
                        mid_idx+=1 
                        end_idx-=1
                        while mid_idx<end_idx and nums[mid_idx]==nums[mid_idx-1]:
                            mid_idx+=1
                        while mid_idx<end_idx and nums[end_idx]==nums[end_idx-1]:    
                            end_idx+=1
            front_idx+=1              
        return threeNum_sum_0
