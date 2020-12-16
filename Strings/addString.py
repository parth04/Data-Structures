415. Add Strings
Easy

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly."""
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        op1 = 0
        op2 = 0
        
        for i in num1:
            op1 = op1*10 + (ord(i) -48)
            
        for j in num2:
            op2 = op2*10 + (ord(j) -48)
            
        return str(op1+op2)


"""
Explanation:
1) The catch here is we can't directly use int() function to convert string into int.
2) Therefore I used ord() function which returns the number representing the unicode code of a specified character. 
3) For greater than 1 digit number I used for loop to iterate over it and convert it to integer.
4) Finally returned the addition in str  

"""
