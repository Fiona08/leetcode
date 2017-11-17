
#150


# Time:  O(n)
# Space: O(n)


# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class stackSol():
    def evaluateReversePolishNotation(self,RPN):
        import operator
        calculation=[]
        operator_lookup={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.floordiv}
        for num in RPN:
            if num not in operator_lookup:
                calculation.append(int(num))
            else:
                num1, num2=calculation.pop(),calculation.pop()
                calculation.append(operator_lookup[num](num2,num1))
        return calculation
