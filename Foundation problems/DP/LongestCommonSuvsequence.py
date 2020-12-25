"""
1143. Longest Common Subsequence
Medium


Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

"""

#Method-1 (Recursive. Might give TLE for long inputs)
class Solution:
    mat  = [[-1 for x in range(1002)] for y in range(1002)]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        res = self.helper(text1, text2, m, n)
        return res
    
    def helper(self, text1, text2, m, n):
        if m==0 or n==0:
            return 0
        if self.mat[m][n] != -1:
            return self.mat[m][n]
        if text1[m-1] == text2[n-1]:
            self.mat[m][n] = 1+ self.helper(text1, text2, m-1, n-1)
            return self.mat[m][n]
        else:
            self.mat[m][n]=max(self.helper(text1, text2, m-1, n),self.helper(text1, text2, m, n-1))
            return self.mat[m][n]

#Method -2 (Bottom up or Memoization approach. All test cases may pass but not time efficient ~2280ms)
class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        mat  = [[-1 for x in range(1002)] for y in range(1002)]
        res = self.helper(text1, text2, m, n, mat)
        return res
    
    def helper(self, text1, text2, m, n, mat):
        if m==0 or n==0:
            return 0
        if mat[m][n] != -1:
            return mat[m][n]
        if text1[m-1] == text2[n-1]:
            mat[m][n] = 1+ self.helper(text1, text2, m-1, n-1, mat)
            return mat[m][n] 
        else:
            mat[m][n]=max(self.helper(text1, text2, m-1, n, mat),self.helper(text1, text2, m, n-1, mat))
            return mat[m][n] 

#Method-3 (Top down approach. Most efficient ~430ms)
class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        mat = [[0 for i in range(n+1)]for j in range(m+1)]
        res = self.helper(text1, text2, m ,n, mat)
        return mat[m][n]
  
    def helper(self, text1, text2, m ,n, mat):
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    mat[i][j] = 1+ mat[i-1][j-1] 
                else:
                    mat[i][j] =  max(mat[i-1][j], mat[i][j-1]) 
        return mat[m][n]

"""
Explanation:https://www.youtube.com/watch?v=hR3s9rGlMTU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=21&ab_channel=AdityaVerma
1) Method 1 - https://www.youtube.com/watch?v=4Urd0a0BNng&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=19&ab_channel=AdityaVerma
2) Method 2 - https://www.youtube.com/watch?v=g_hIx4yn9zg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=20&ab_channel=AdityaVerma
3) Method 3 - https://www.youtube.com/watch?v=hR3s9rGlMTU&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=21&ab_channel=AdityaVerma

"""
        
        
