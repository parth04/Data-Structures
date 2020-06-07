
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false

"""



class Solution:
    def isValid(self, s: str) -> bool:
        s = (list(s))
        left_opening = ['[','{','(']
        right_opening = [']','}',')']
        stack = []
        
        for i in s:
            if i in left_opening:
                stack.append(i)
                continue
            
            if len(stack) > 0 and left_opening[right_opening.index(i)] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
              
"""
Explanation:
1)Push all the opening brackets in the stack.
2)Once you encounter closing bracket, popcompare the top most bracket from stack and with encountered bracket. If it matches, pop the stack.
3)Continue this untill stack is not empty.
4)For comparing brackets you can use two list of opening and closing brackets or can also use Dictionary(key:value) i.e. {'(':')'}       

"""

