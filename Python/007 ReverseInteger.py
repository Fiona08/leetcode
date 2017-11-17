#7


# Space: O(1)


# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
# Input: 123
# Output:  321
# Example 2:
# Input: -123
# Output: -321
# Example 3:
# Input: 120
# Output: 21
# 
# Note:
# Assume we are dealing with an environment
# which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.


class mathSol():
    def reverseInteger(self,num):
        if num<0:
            return -self.reverseInteger(-num)
        reversed_int=0
        while num:
            reversed_int=reversed_int*10+num%10
            num//=10
        return reversed_int if reversed_int <= 0x7fffffff else 0
