"""
435. Non-overlapping Intervals
Medium

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #This is greedy problem. Very imp 1st step is sort the list in ASC order.
        intervals = sorted(intervals)
        total = len(intervals)
        left = 0
        right = 1
        
        while right < len(intervals): #Iterate the right pointer till end of the list.
            
            #Case 1: When there is no overlapping, increment the left upto right pointer and increment right pointer by 1. 
            if intervals[right][0] >= intervals[left][1]:
                left=right
                right+=1
                continue
                
            #Case 2: If interval left is ending before interval right then simply remove the right interval. That means increment right by 1     
            if intervals[left][1] <= intervals[right][1]:
                right+=1
                total-=1
                continue
            
            #Case 3: If interval left is ending after interval right then simply remove the left interval. That means increment the left upto right pointer and increment right pointer by 1
            if intervals[left][1] > intervals[right][1]:
                left=right
                right+=1
                total-=1
                continue
           
         
        return len(intervals) - total
