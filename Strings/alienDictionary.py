"""
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

"""

#Method 1
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordDict = {} 
        ans = []
        for i in range (len(order)):
            ordDict[order[i]] = i
        # print("ordDict: ",ordDict)
        
        for i in range(len(words) -1 ):
            word1 = words[i]
            word2 = words[i + 1]
            smallerWordLength = min(len(word1), len(word2))
            for j in range(smallerWordLength):
                if ordDict[word1[j]] > ordDict[word2[j]]:
                    return False
                elif ordDict[word1[j]] < ordDict[word2[j]]:
                    break
                elif ordDict[word1[j]] == ordDict[word2[j]]:
                    continue

	    #The else block just after for/while is executed only when the loop is NOT terminated by a break statement.
            else:
                if len(word1) > len(word2):
                    return False
        return True


#Method 2
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordDict = {} 
        ans = []
        for i in range (len(order)):
            ordDict[order[i]] = i
        # print("ordDict: ",ordDict)
        
        for word in words:
            temp = []
            for ch in word:
                temp.append(ordDict[ch])
            ans.append(temp)
        # print("Ans - ",ans)
        
        return sorted(ans) == ans
            


"""
Explanation:

Method1 (More efficient, less intuitive)-
1) First thing first, make a dictionary of order.
2) First for loop is used to iterate through all the words in words[]. We need to compare each char from 2 words in words[]. To avoid array index out of bound error we iterate over min length between 2 words i.e word1 and word2.
3) If value of char from word1 in dictionary is greater than value of char from word1 then return false. If value is same, check next char. if values is less than word2 char then continue the outer for loop.
4) The most imp condition is to check if len(word1) > len(word2). But check this condition only when there is no inner loop is not terminated by break condition. 
5) Only in python we can write for/while-else statements.

Method2 (Less efficient, More intuitive)-
1) First thing first, make a dictionary of order.
2) Iterate through all the elements in words[] and create list of list of dictionary values of each char in word. 
3) Lastly, comapre if sorted list  == original list. If it is then return True else return false. 


"""
