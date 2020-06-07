
"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

"""

class Solution:
    def addDigits(self, num: int) -> int:
        
        res = self.addition(num)
        addition2(num)
        while res >= 10:
            res = self.addition1(res)
        return res
        
    def addition1(self,num):
        output = []
        q,r =divmod(num,10)
        output.append(r)
        while q > 10:
            q,r = divmod(q,10)
            output.append(r)
        output.append(q)
        return sum(output)


     def addition2(self, num: int) -> int:
        if num == 0:
            return 0
        elif num%9 ==0:
            return 9
        else:
            return num%9
        




"""
1) Stored the every single digit of given number in a list. Check if addition of that list is >= 10 else repeat the same method.
2) 2) Check addition2 method also.
"""
