"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#	  Method-1(Brute Force n**3 complexity)
#         if not s:
#             return 0
#         start =0
#         end =0
#         length = len(s)
#         if length == 1:
#             return 1
#         temp = ""
#         ans = []
        
        
        
#         for i in range(length):
#             temp = s[i]
#             for j in range (i+1,length):
#                 if s[j] not in temp:
#                     temp+=s[j]
#                 else:
#                     break
#             ans.append(len(temp))
#         return max(ans)
        #Method -2 (Optimized)
        length = len(s)
        ans = 0
        charDict = {}
        anchor = 0
        
        for j in range(length):
            if s[j] in charDict:
                anchor = max(charDict[s[j]], anchor) #We are not taking anchor = charDict[s[j]] + 1 because consider this "abba" example. For last a anchor will go to index 2 which is wrong, anchor can't go backward
            ans = max(j-anchor+1, ans) #Calculating the length of substring. 
            charDict[s[j]] = j+1
        return ans
                

"""

Explanation: 
Method -1
1) The main idea here is, start with char at every  index and check if there any duplicate char in s[idx:].
2)Whenever there is duplicate, break the inner loop and store length in temp list.
3) Return the max of list

Method-2
1) Create a dict of unique char and whenever duplicate found move the anchor to index where duplicate found.
2) For more explanation watch video from 13:18 to 14:12.
https://www.youtube.com/watch?v=qtVh-XEpsJo&ab_channel=takeUforward
"""
