"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0

"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = {} # map each (r,c) ------> max length of square
        
        
        
        
        def helper(r, c, matrix):
            rows = len(matrix)
            cols = len(matrix[0])
            if r >=rows or c >= cols:
                return 0

            if (r,c) not in cache:
                down = helper(r+1,c,matrix) 
                right = helper(r,c+1,matrix)
                diagonal = helper(r+1,c+1,matrix)

                cache[(r,c)] = 0 
                if matrix[r][c] == "1":
                    cache[(r,c)]= 1+ min(down,  right,diagonal)
            return cache[(r,c)]
        helper(0,0,matrix)
        return max(cache.values())**2

"""
Explanation:
1) Solved by seeing following video. https://www.youtube.com/watch?v=6X7Ha2PrDmM&feature=emb_title&ab_channel=NeetCode

"""
