 #154


# Time:  O(logn)
# Space: O(1)


# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.


 class binarySearchSol():
    def minInRotatedValueII(self,nums):
        left,right,last_val=0,len(nums)-1,nums[-1]
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>last_val:
                left=mid+1
            else :
                right=mid-1
        return nums[left]
