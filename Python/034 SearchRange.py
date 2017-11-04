#34


# Time:  O(logn)
# Space: O(1)


# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class binarySearchSol():
    def searchRange(self,nums,target):
        left=self.binarySearch2(nums,target,lambda x,y:x>=y)
        print(left)
        if left>=len(nums) or nums[left]!=target:
            return [-1,1]
        right=self.binarySearch2(nums,target,lambda x,y:x>y)
        return [left,right-1]
    
    # most left
    def binarySearch1(self,nums,target,compare=lambda x,y:x>=y):
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if compare(nums[mid],target):
                right=mid-1
            else:
                left=mid+1
        return left
    
    
    def binarySearch2(self,nums,target,compare=lambda x,y:x>=y):
        left,right=0,len(nums)
        while left<right:
            mid=(left+right)//2
            if compare(nums[mid],target):
                right=mid
            else:
                left=mid+1
        return left
    
    def binarySearch3(self,nums,target,compare=lambda x,y:x>=y):
        left,right=-1,len(nums)
        while left+1<right:
            mid=(left+right)//2
            if compare(nums[mid],target):
                right=mid
            else:
                left=mid
        return right
