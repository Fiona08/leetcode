#80 


# Time:  O(n)
# Space: O(1)


# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# Your function should return length = 5,
# with the first five elements of nums being 1, 1, 2, 2 and 3. 
# It doesn't matter what you leave beyond the new length.


class arraySol():
    def removeDupII(self,nums):
        unique_len,times=0,1
        for idx in range(1,len(nums)):
            if nums[idx]!=nums[unique_len]:
                unique_len+=1
                nums[unique_len]=nums[idx]
                times=1
            elif times<2:
                unique_len+=1
                nums[unique_len]=nums[idx]
                times+=1
            else:
                times=0
        return unique_len+1
