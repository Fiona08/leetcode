#205


# Time:  O(n)
# Space: O(n)


# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character
# while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
# Given "foo", "bar", return false.
# Given "paper", "title", return true.


class hashTableSol():
    def isomorphicString(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        str1_to_str2,str2_to_str1={},{}
        for char1,char2 in zip(str1,str2):
            if char1 not in str1_to_str2 and char2 not in str2_to_str1:
                str1_to_str2[char1],str2_to_str1[char2]=char2,char1
            elif str1_to_str2[char1]!=char2 or str2_to_str1[char2]!=char1:
                return False
        return True
