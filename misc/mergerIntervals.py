"""
56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals) #Sort the list.
        j=1
        ans = []
        stack = [intervals[0][0],intervals[0][1]] #append 1st pair of interval in stack.
        while j < len(intervals): #starting J from 2nd pair or index 1.
            if intervals[j][0] <= stack[-1]: #Check if interval[j][0] is smaller than top of stack.
                if intervals[j][1] > stack[-1]: #and interval[j][1] > top of stack. for example [[1,4],[2,3]].
                    stack.append(intervals[j][1])
                j+=1
            else:
                ans.append([stack[0],stack[-1]]) #Append the first and last element of stack in final ans as a one interval.
                stack.clear() #Clear the stack
                stack.append(intervals[j][0]) #Again add the jth interval where if condition filed. 
                stack.append(intervals[j][1])
                j+=1
        ans.append([stack[0],stack[-1]]) #Append the last pair of interval in stack to the final ans.
        # print("ans = ",ans)
        return ans
            

"""
Explanation:
1) Firts thing we should always remeber that, whenever there is need to traverse the list again and agian in the same direction then 100% of times we can use stack.
2) Foremost thing in interval problems is to sort the given list. Therefore I sorted the list.
3) Add the start and end of 1st interval in stack. Starting with J=1 check if start of jth interval is smaller than or equal to top of stack. If not then that means continuity of overlapping is breaked, therefore append the 1st and last element of stack to the ans.
4) At last stack will contain last interval in list so append it too to the ans.

"""
