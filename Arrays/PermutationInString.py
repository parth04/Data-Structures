"""

567. Permutation in String
Medium

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_counter = Counter(s1)
        window = Counter()
        # print("S1 Counter:",s1_counter)

        for key,val in enumerate(s2):
            # print("Key", key)
            window[val]+=1
            if key >= len(s1):
                if window[s2[key - len(s1)]] == 1:
                    del window[s2[key - len(s1)]] #If char has only 1 freq, delete it.
                else:
                    window[s2[key - len(s1)]] -= 1 #If char has more than 1 freq, decrease it by one.
            if window == s1_counter:
                return True
        return False

"""
Explanation:
1) I used the sliding window technique here.
2) The main idea here is we can only find permutation of string1 in string2 if and only if we have equal numbers of chars in string2 as of in string1. To get the count of every chsr in string I used Counter.
	example: - s1='ab'	s2='eidbaooo'
		a-1, b-1
3)Consider a window of length s1, move it over s2 starting from 0th position and check if s1 == window. If not move window by one position.	  

"""
