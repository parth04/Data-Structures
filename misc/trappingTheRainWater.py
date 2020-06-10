"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        temp = []
        left, right,water = 0,0,0
        for i in height:
            left = max(left, i)
            temp.append(left)
        temp.reverse()
        for i, val in enumerate(reversed(height)):
            right  = max(right, val)
            water = water + min(temp[i], right) -val
        return water            
                
        
#	 n = len(height)
#         if height == [] or height.count(0) == n-1:
#             return 0
        
#         x = max(height)
#         first_max=height.index(x)
#         last_max=(n - 1) -height[::-1].index(x)
#         pivot = 0
#         current =0
#         idx_current = 0
#         idx_pivot = 0
#         water = 0

#         while idx_pivot < last_max:
#             for i in range (idx_current,first_max+1):
#                 if height[i] > 0 or height[i] != x:
#                     current = height[i]
#                     idx_current = i
#                     break
#             for i in range(idx_current,last_max+1):
#                 if height[i+1] >= height[idx_current]:
#                     pivot = height[i+1]
#                     idx_pivot = i+1
#                     break
#             if idx_pivot - idx_current != 0:
#                 min_val = min(current, pivot)
#                 for i in range (idx_current+1,idx_pivot):
#                     water = water + (min_val - height[i])
#                 current = pivot
#                 idx_current = idx_pivot
                
                
#         idx_pivot = n-1
#         idx_current = n-1
#         while idx_pivot > last_max:
#             for i in range(idx_current, last_max-1,-1):
#                 if height[i] > 0 or height[i] != x:
#                     current = height[i]
#                     idx_current =  i
#                     break

#             for i in range(idx_current, last_max-1,-1):
#                 if height[i - 1] >= height[idx_current]:
#                     pivot = height[i - 1]
#                     idx_pivot = i - 1
#                     break

#             if idx_current - idx_pivot != 0:
#                 min_val = min(current, pivot)
#                 for i in range (idx_current-1,idx_pivot,-1):
#                     water = water + (min_val - height[i])
#                 current = pivot
#                 idx_current = idx_pivot

#         return water



"""
Description(of commented code)
1) Firstly check if list is empty or there is only and only one building in the list. (Means apart from 1 element all other elements are zero)
2)Calculate the first max and last max from the list.
3)Iterate till pivot is not at last max.
starting from index 0, find the first buildind. Store the value and index.
4)After finding current, find next highest building and make it pivot.
5)Check if there is gap in between buildings or not.
If there is gap, fill all the elements excluding current and pivot with (min_val between current and pivot) minus (height of that building)
6) Repeat the same procedure traversing list from last index. 

"""
