
"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        int_n =self.sqrDigits(n)

        while sum(int_n) != 1:
            int_n = self.sqrDigits(sum(int_n))
            if sum(int_n) == 4:
                return False
        return True
    
    def sqrDigits(self,n):
        n = list(str(n))
        int_n = []
        for i in range(len(n)):
            int_n.append(int(n[i])**2)
        return int_n


"""
# Method of solving
#
# 1. Convert the given number into a list of digits of type int
# 2. Find the sum of squares of each digits
# 3. if the sum is equal to 1, then it is a happy number
# 4. if the sum of squares comes out to be 4, then there starts a cycle of numbers for sum which is 4→16→37→58→89→145→42→20→4.
# This cycle keeps on repeating. Hence, we can terminate the code when we detect the start of this cycle which is 4,
# concluding that it is not a happy number.

"""
