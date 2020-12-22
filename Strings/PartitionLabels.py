"""
763. Partition Labels
Medium

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

"""

class Solution:
    #Method-1
    def partitionLabels(self, S: str) -> List[int]:
        countDict ={}
        idxDict = {}
        subStr = ""
        ans = []
        # final = []
        for key,val in enumerate(S):
            if val in countDict:
                countDict[val]+=1
            else:
                countDict[val] = 1
                
        # print("countDict = ",countDict)
        
        for char in S:
            subStr+=char
            res = self.helper(subStr,countDict)
            if res == False:
                continue
            else:
                ans.append(res)
                subStr = "" #Emptying the substring coz it suppose to hold string of next partition.
        
        # for item in ans:
        #     final.append(len(item))
        return ans
        # print("Ans = ",ans)
        # print("--------------------------------------------------------------------------")
        # print("idxDict = ",idxDict)
        # print("--------------------------------------------------------------------------")
        # print("countDict = ",countDict)
    
    
    #Method-2
    def helper(self, subStr, countDict):
        for char in subStr:
            if all(subStr.count(char) == countDict[char] for char in subStr):
                return len(subStr)
            else:
                return False

        last = {c: i for i, c in enumerate(S)}
        print("Last = ", last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c]) #As we are moving sequentially over S, when index of curr char matches with the last index of same char in S that time we can say "each letter appears in at most one part."
            if i == j:
                ans.append(i - anchor + 1) #Subtracting anchor because when we will find second partion, the value of i will be index of last partition. So we need to store the end of previous partition into Anchor and then subtracting it from last index of next partition
                anchor = i + 1
            
        return ans


"""
Explanation:
Method-1(More intuitive. Kinda brute-force)
1) First create dictionary of every char in S with their count.
2) Consider every char from string S,create substring of it and send it to helper function.
3) In helper function again iterate over complete substring and check if count of every char in substring is equal to count of that char in dictionary. If the count is same return length of that substring, else return False.
4) Back in main fuction check if helper returns false, then continue the for loop by appending next char to substirng, else append length to final list and empty the substrng.


"""
