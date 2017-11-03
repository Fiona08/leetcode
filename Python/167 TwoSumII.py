#167



# Time:  O(n)
# Space: O(1)


# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers 
# such that they add up to the target, where index1 must be less than index2. 
# Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2



class twoPointerSol():
    def twoSumII(self,nums,target):
        start, end=0,len(nums)-1
        while start<end:
            cur_sum=nums[start]+nums[end]
            if cur_sum<target:
                start+=1
            elif cur_sum>target:
                end-=1
            else:
                return [start+1,end+1]
        return []
