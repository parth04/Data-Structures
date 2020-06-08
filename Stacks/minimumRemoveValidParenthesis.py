
"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

"""



class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        str_list = list(s)
        opening_bracket = ['(']
        closing_bracket = [')']
        stack = []
        index =[]
        
        for i in range(len(s)):
            if s[i] in opening_bracket:
                stack.append(s[i])
                index.append(i)
                continue
            elif s[i] in closing_bracket and len(stack) == 0:
                index.append(i)
                continue
            elif s[i] in closing_bracket and len(stack) != 0:
                stack.pop()
                index.pop()
        
        if len(index) != 0:
            while len(index) != 0:
                str_list.pop(index.pop())
        return "".join(str_list)





	# for i in s:
        #     if i in opening_bracket:
        #         stack.append(i)
        #         continue
        #     elif i in closing_bracket and len(stack) == 0:
        #         str_list.remove(i)
        #         continue
        #     elif i in closing_bracket and len(stack) != 0:
        #         stack.pop()
        # if len(stack) != 0:
        #     str_list.reverse()
        #     while len(stack) != 0:
        #         str_list.pop(str_list.index(stack.pop()))
        #     str_list.reverse()
        # return "".join(str_list)




"""
Explanation:
1)First convert string into list. After that iterate over length of string or list.
2)If element is open bracket then push it onto the stack[] and push index[] of that element  in the index stack.
3)If element is closing bracket then check if stack is empty or not. If it is empty store the index of it in index[]. If stack[] is not empty then pop the stack element as well as index element.
4)After iterating the whole string, check if index is empty or not. Here we are not checking whether stack is empty or not because if closing bracket appear when stack is empty then simply we are not string it's index in index[].
5)While index is not empty delete the element from str_list from position store in index[]. i.e. str_list.pop(index.pop())

"""
