#219 


# Time:  O(n)
# Space: O(n)


# Given an array of integers and an integer k, return true
# if and only if there are two distinct indices i and j in the array 
# such that nums[i] = nums[j] and the difference between i and j is at most k.


class hashTableSol():
    def containDuplicateII(self,nums,max_distance): 
        num_indice={}
        for indice,num in enumerate(nums):
            if num in num_indice:
                if indice-num_indice[num]<=max_distance:
                    return True
                num_indice[num]=indice
            else:
                num_indice[num]=indice
        return False
                
