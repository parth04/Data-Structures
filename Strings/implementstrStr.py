"""
28. Implement strStr()
Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
#Method 1:
        if needle == "":
            return 0
        
        if needle in haystack:
            return haystack.index(needle)
        
        return -1

#Method 2:

#         if needle == "":
#             return 0
    
        
#         for i in range(len(haystack) - (len(needle) - 1)):
#             if haystack[i: i+len(needle)] == needle:
#                 return i
                
        
#         return -1



"""
Explanation:

1) Method 1(Runtime ~40ms). This is very intuitive method. First check if needle is present in haystack or not, if it present then use built in fuction of python i.e str.index() which returns index of substring from where it starts. Example s= "Hello", t= "ll". s.index("ll") will return 2.

2) Method 2(Runtime ~20ms). In this method range in for loop is very important. Because if we use range(len(haystack)) then there would be too many unnecessarly comparisons. Instead what we did is we started from index equal to (len(haystack) - (len(needle) - 1) which is length of needle.  

"""


