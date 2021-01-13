"""
784. Letter Case Permutation
Medium

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]

"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S.isnumeric():
            return [S]
        ip = S
        op = ""
        ans = []
        res = self.helper(ip, op, ans)
        # print("Res = ", res)
        return res
    def helper(self, ip, op, ans):
        if len(ip) == 0:
            ans.append(op)
            return 
        if ip[0].isalpha():
            op1 = op
            op2 = op
            op1+=ip[0].lower()
            op2+=ip[0].upper()
            self.helper(ip[1:],op1,ans)
            self.helper(ip[1:],op2,ans)  
        else:
            op3 = op
            op3+=ip[0]
            self.helper(ip[1:],op3,ans)
        return ans

"""
Explanation:

1) For detailed explanation watch "https://www.youtube.com/watch?v=4eOPYDOiwFo&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=16&ab_channel=AdityaVerma"

"""

