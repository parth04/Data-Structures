"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        optr = []
        post = []
        output = []
        digit = ''
	
	#Handling the special case if there is only single digit
        if s.isnumeric():
            return int(s)

	#Converting the input into postfix notation
        for i in s[::-1]:
            if i == ')' or i == '+' or i == '-':
                if digit != '':
                    post.append(int(digit))
                    digit =''
                optr.append(i)
                continue
                
            if i.isnumeric():
                digit = i + digit
                continue
            if i == '(':
                post.append(int(digit))
                digit = ''
                while optr[-1] != ')':
                    post.append(optr.pop())
                optr.pop()
        if digit != '':
            post.append(int(digit))
            digit = ''
	#Checking if operator stack is empty or not if it is not then pushing all the data in that stack
        if optr:
            while optr:
                post.append(optr.pop())

	#Performing basic operation
        for i in post:
            if i == '+':
                op1 = output.pop()
                op2 = output.pop()
                output.append(op1 + op2)
                continue
            if i == '-':
                op2 = output.pop()
                op1 = output.pop()
                output.append(op2 - op1)
                continue
            else:
                output.append(i)
        return output[-1]
