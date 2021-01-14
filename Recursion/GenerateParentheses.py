"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        v = []
        openn = n
        close = n
        op = ""
        return self.helper(openn, close, op, v)

    def helper(self, openn, close, op, v):
        if openn ==0 and close ==0: #Base Condition is when count of open and close brackets are zero, we get 1 combination of valid parenthesis
            v.append(op)
            return v
        if openn!=0: #We are getting choice of using opening bracket when it is not zero
            op1 = op
            op1+="("
            self.helper(openn-1, close, op1, v)
        if close > openn: #This is crusial condition. In this We can use closing bracket only when close > open i.e when there is already a open bracket then only we can use close bracket.
            op2 = op
            op2+=")"
            self.helper(openn, close-1, op2, v)
        return v

"""
Explanation:
1) For detail explanation see "https://www.youtube.com/watch?v=eyCj_u3PoJE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17&ab_channel=AdityaVerma"

"""


