#31


# Time:  O(n)
# Space: O(1)


# Implement next permutation, which rearranges numbers
# into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange 
# it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class arraySol():
    def nextPermutation(self,nums):
        last_smaller_idx,least_greater_idx=-1,0
        for idx in range(len(nums)-1):
            if nums[idx]<nums[idx+1]:
                last_smaller_idx=idx
        if last_smaller_idx==-1:
            return nums.reverse()
        for idx in range(last_smaller_idx+1,len(nums)):
            if nums[idx]>nums[last_smaller_idx]:
                least_greater_idx=idx
        nums[last_smaller_idx],nums[least_greater_idx]=nums[least_greater_idx],nums[last_smaller_idx]
        nums[last_smaller_idx+1:]=nums[:last_smaller_idx:-1]
        return nums
