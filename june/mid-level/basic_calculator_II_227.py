########################################################################
#
#   @author:        yusuufaslan
#   @date:          03.06.2023
#   @problem:       227. Basic Calculator II
#
########################################################################


class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0

        prev_operator = '+'
        s += '+'
        stack = []

        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c == ' ':
                pass
            else:
                if prev_operator == '+':
                    stack.append(num) 
                elif prev_operator == '-':
                    stack.append(-num)
                elif prev_operator == '*':
                    operand = stack.pop()
                    stack.append(operand * num)
                elif prev_operator == '/':
                    operand = stack.pop()
                    stack.append(int(operand / num))
                num = 0
                prev_operator = c
        
        return sum(stack)

"""
Problem Description:
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""