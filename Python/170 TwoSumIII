#170


# Time:  O(n)
# Space: O(n)


# Design and implement a TwoSum class. It should support the following operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
# 
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false


class twoSumIII():
    def __init__(self):
        self.num_count={}
    
    def add(self,val):
        if val in self.num_count:
            self.num_count[val]+=1
        else:
            self.num_count[val]=1
    
    def find(self,target):
        for num in self.num_count:
            if target-num in self.num_count and (target-num!=num or self.num_count[target-num]>1):
                return True
        return False
