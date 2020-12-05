"""
125. Valid Palindrome
Easy

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(i for i in s if i.isalnum()).lower()
        
        return s == s[::-1]
        
#         if s == s[::-1]:
#             return True
#         else:
#             return False



"""
Explanation:
1) Very easy problem. Store all the numbers and alphabet in variable as string. Convert all the alphabets in either lowe or upper case.
2)Simply compare that string with reverse of itself i.e. if s == s[::-1]

"""
        
