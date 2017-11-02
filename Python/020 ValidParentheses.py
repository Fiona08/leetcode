#20


# Time:  O(n)
# Space: O(n)


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.


class stackSol():

    def validParentheses(self,string):
        stack,parentheses_pairs=[],{'}':'{',']':'[',')':'('}
        for parenthese in string:
            if parenthese not in parentheses_pairs.keys():
                stack.append(parenthese)
            elif len(stack)==0 or parentheses_pairs[parenthese]!=stack.pop():
                return False
        return len(stack)==0
