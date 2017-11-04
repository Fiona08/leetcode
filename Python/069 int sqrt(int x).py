 #69


# Time:  O(logn)
# Space: O(1)

 
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.


class binarySearchSol():
    def mysqrt(self,num):
        if num <2:
            return num
        left, right=1,num//2
        while left<=right:
            mid=(left+right)//2
            if mid*mid>num:
                right=mid-1
            else:
                left=mid+1
        return left-1
