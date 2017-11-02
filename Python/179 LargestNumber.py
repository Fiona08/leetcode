#179
  
  
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.    


class sortSol():
    def largestNumber(self,nums):
        nums=[str(x) for x in nums]
        nums.sort(key=cmp_to_key(lambda x,y:int(y+x)-int(x+y)))
        return ''.join(nums).lstrip('0') or '0'
