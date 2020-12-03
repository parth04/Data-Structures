"""
387. First Unique Character in a String
Easy

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        sCounter = Counter(s)
        sDict = {}
        for key,val in sCounter.items():
            # print(key, val)
            if val == 1:
                sDict[s.index(key)] = key
        # print("Dict",sDict)
        if not sDict:
            return -1
            
        return min(sDict.keys())


"""
Explanation:

1) My thought process here was to first calculate the frequence of each letter hats why I used counter.
2) But problem here is we need to return the index number so I created dictionary of chars with frequence where key is index number and val is char. 
3) As we know there is only one occurance, so I used str.index() method as it returns index of 1st occurance of word.
4) While returning simply returned the min of key values in dictionary.
"""
