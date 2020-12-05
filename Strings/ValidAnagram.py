"""
242. Valid Anagram
Easy

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        
        # print("s_counter: ",s_counter)
        # print("t_counter: ",t_counter)  
        
        if s_counter == t_counter:
            return True
        else:
            return False


"""
1)The main idea here is to check the anagram, both the strings must have same length. So if len is not same return false then and there.
2)Else check the freq of each char in s with freq of each char in t. If matches return true else return false.

"""
