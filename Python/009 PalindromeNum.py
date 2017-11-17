#9


# Determine whether an integer is a palindrome.
# Do this without extra space.


class mathSol():
    def palindromeNum(self,num):
        if num<0:
            return False
        num_copy,reversed_num=num,0
        while num_copy:
            reversed_num=reversed_num*10+num_copy%10
            num_copy//=10
        if reversed_num==num:
            return True
