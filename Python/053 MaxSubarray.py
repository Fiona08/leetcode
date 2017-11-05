#53


# Time:  O(n)
# Space: O(1)


# Find the contiguous subarray within an array
# (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class DynamicProgrammingSol():
    def maxSubarray1(self,nums):
        if max(nums)<0:
            return max(nums)
        local_max,global_max=0,float('-Inf')
        for num in nums:
            local_max=max(0,local_max+num)
            global_max=max(global_max,local_max)
        return global_max
    def maxSubarray2(self,nums):
        sum_by_far,min_sum_by_far,max_sum=0,0,float('-Inf')
        for num in nums:
            sum_by_far+=num
            max_sum=max(max_sum,sum_by_far-min_sum_by_far)
            min_sum_by_far=min(min_sum_by_far,sum_by_far)
        return max_sum
