#169


# Time:  O(n)
# Space: O(1)


# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty 
# and the majority element always exist in the array.


class arraySol():
    def majorityElem(self,nums):
        majority_elem=[]
        for elem in nums:
            if len(majority_elem)==0:
                majority_elem.append(elem)
            elif elem!=majority_elem[-1]:
                majority_elem.pop()
            else :
                majority_elem.append(elem)
        return majority_elem[0]
