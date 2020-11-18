"""
438. Find All Anagrams in a String
Medium


Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        window = Counter()
        result = []
        # print("P_counter", p_counter)
        for key,val in enumerate(s):
            window[val]+=1
            print("Window iteration",key, window)
            if key >= len(p):
                if window[s[key - len(p)]] == 1:
                    del window[s[key - len(p)]]
                else:
                    window[s[key - len(p)]] -= 1
            print("Window after iteration",key,window)
            
            if window == p_counter:
                result.append(key-len(p)+1)
        # print("Result:",result)
        return result

"""
Explanation:
1) I used the sliding window technique here.
2) The main idea here is we can only find permutation of string1 in string2 if and only if we have equal numbers of chars in string2 as of in string1. To get the count of every chsr in string I used Counter.
	example: - s1='ab'	s2='eidbaooo'
		a-1, b-1
3)Consider a window of length s1, move it over s2 starting from 0th position and check if s1 == window. If not move window by one position.
4)When s1 == window matches then calculate the index and store it.

"""

