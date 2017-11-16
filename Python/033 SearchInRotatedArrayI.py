#33


# Time:  O(logn)
# Space: O(1)


# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.


class binarySearchSol():
    def searchInRotatedArrayI(self,nums,target):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif (nums[mid]>nums[left] and nums[left]<=target<nums[mid]) or \
                 (nums[mid]<nums[left] and not (nums[mid]<target<=nums[right])):
                right=mid-1
            else:
                left=mid+1
        return -1
