#136


# Time:  O(n)
# Space: O(1)


# Given an array of integers, every element appears twice except for one. 
# Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?


class bitManiputationSol():
    def singleNumber1(self,nums):
        from functools import reduce
        return reduce(lambda x,y:x^y,nums)
    def singleNumber2(self,nums):
        import operator
        from functools import reduce
        return reduce(operator.xor,nums)
