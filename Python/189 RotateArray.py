#189


# Time:  O(n)
# Space: O(1)


# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, 
# the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, 
# there are at least 3 different ways to solve this problem.

class arraySol():
    def rotateArray1(self,nums,k):
        nums[:]=nums[-k:]+nums[:-k]
        
        
    def rotateArray2(self,nums,k):
        self.reverse(nums,0,len(nums)-1)
        print(nums)
        self.reverse(nums,0,k-1)
        print(nums)
        self.reverse(nums,k,len(nums)-1)
    
    def reverse(self,nums,start_idx,end_idx):
        while start_idx<end_idx:
            nums[start_idx],nums[end_idx]=nums[end_idx],nums[start_idx]
            start_idx,end_idx=start_idx+1,end_idx-1
