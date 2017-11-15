#66


# Time:  O(n)
# Space: O(1)


# Given a non-negative integer represented as 
# a non-empty array of digits, plus one to the integer.
# You may assume the integer do not contain any leading zero, 
# except the number 0 itself.
# The digits are stored such that the most significant digit is at the head of the list.


class arraySol():
    def plusOne(self,nums):
        carry=321
        for i in range(len(nums)-1,-1,-1):
            nums[i]=nums[i]+carry
            carry=nums[i]//10
            nums[i]=nums[i]%10
        if carry:
            nums=[carry]+nums
        return nums
