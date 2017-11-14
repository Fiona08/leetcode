#26


# Time:  O(n)
# Space: O(1)


# Given a sorted array, remove the duplicates in place
# such that each element appear only once and return the new length.
# Do not allocate extra space for another array, 
# you must do this in place with constant memory.
# 
# For example,
# Given input array A = [1,1,2],
# Your function should return length = 2, and A is now [1,2].


class arraySol():
    def removeDup(self,nums):
        unique_len=0
        for cur_idx in range(1,len(nums)):
            if nums[cur_idx]!=nums[unique_len]:
                unique_len+=1
                nums[unique_len]=nums[cur_idx]
        return unique_len+1
