#217


# Time:  O(n)
# Space: O(n)


# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.

class hashTableSol():
    def containDuplicate1(self,nums):
        return len(nums)>len(set(nums))
    #217    
    def containDuplicate2(self,nums):
        num_appear_by_far={}
        for num in nums:   
            if num in num_appear_by_far:
                return True
            else:
                num_appear_by_far[num]=True
        return False
