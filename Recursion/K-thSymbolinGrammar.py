"""
779. K-th Symbol in Grammar
Medium

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N==1 and K==1: #This is the base condition given in the problem
            return 0
        mid = pow(2,N-1)//2 #We found out the pattern that for any N the first half bits are similar to bits of N-1 row. Also, for any N second half bits are compliment of bits of N-1 row.
        if K<=mid: #Therefore if K <= half then we can simply return the bit from N-1 row
            return self.kthGrammar(N-1,K)
        else: #Otherwise we returnd the compliment. We did K-mid to get index correcpondance to N-1 row.
            return self.kthGrammar(N-1,K-mid)^1


"""
Explanation:
1) Must watch video for detailed explanation "https://www.youtube.com/watch?v=5P84A0YCo_Y&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10&ab_channel=AdityaVerma"
"""
