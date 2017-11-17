#60


# The set [1,2,3,…,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.



class mathSol():
    def permutationSequence(self,n,k):
        import math
        perm_num=[ _ for _ in range(1,n+1)]
        subseq_nums=math.factorial(n-1)
        kth_seq=''
        for i in reversed(range(n)):
            if k%subseq_nums:
                cur_num=perm_num[k//subseq_nums]
            else:
                cur_num=perm_num[k//subseq_nums-1]
            kth_seq+=str(cur_num)
            perm_num.remove(cur_num)
            if i>0:
                k%=subseq_nums
                subseq_nums//=i
        return kth_seq
