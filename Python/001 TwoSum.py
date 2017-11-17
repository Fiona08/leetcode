#1


# Time:  O(n)
# Space: O(n)


# Given an array of integers, return indices of 
# the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class hashTableSol():
    def twoSum(self,nums,target):
        num_idx={}
        for idx,num in enumerate(nums):
            if target-num in num_idx:
                return [num_idx[target-num],idx]
            else:
                num_idx[num]=idx
        return []
