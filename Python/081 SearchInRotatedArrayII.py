#81


# Time:  O(logn)
# Space: O(1)


# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.


class binarySearchSol():
    def searchInRotatedArrayII(self,nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            #elif nums[left]==nums[mid]:
            #    left+=1
            elif (nums[mid]>=nums[left] and nums[left]<=target<nums[mid]) or \
                (nums[mid]<nums[left] and not(nums[mid]<target<=nums[right])):
                right=mid-1
            else:
                left=mid+1
        return False
