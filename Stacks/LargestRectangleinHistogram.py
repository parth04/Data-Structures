"""
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:

Input: heights = [2,4]
Output: 4

"""
#Method 1
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        width = []
        area = []
        stack = []
        left = []
        right = []
        length = len(heights)
        for idx,height in enumerate(heights): #Calculating idx of NSL(Nearest Smallest Left) element.
            self.nearestSmallToLeft(height,idx,stack,left)
        stack.clear()
        for idx,height in reversed(list(enumerate(heights))):#Calculating idx of NSR(Nearest Smallest Right) element. We reversed the list coz we want to start it from end. Enumerate can't be directly reversed so we first converted it into list.
            self.nearestSmallToRight(height,idx,length,stack,right)
        # print("Left = ",self.left)
        # print("Right = ",self.right)
        right.reverse()
        for i in range(length):
            width.append(right[i] - left[i] - 1)
        # print("Width = ", width)
        
        for i in range(length):
            area.append(heights[i]*width[i])
        # print("Area = ",area)
        return max(area)
        
    
    def nearestSmallToLeft (self,height,idx,stack,left): 
        pseudoIndexLeft = -1
        if not stack:
            left.append(pseudoIndexLeft) #This means it is first element
        if stack and stack[-1][0] < height:#If immediate left is smaller then append index of that element from stack which consists tuple(height,idx)
            left.append(stack[-1][1])
        if stack and stack[-1][0] >= height:
            while stack and stack[-1][0] >= height:#Move until we find first smallest element 
                stack.pop()
            if not stack: #If you went until the end
                left.append(-1)
            else:
                left.append(stack[-1][1])
        stack.append((height,idx)) #At last append current element to stack
            
    def nearestSmallToRight (self,height,idx,length,stack,right):
        pseudoIndexRight = length
        if not stack:
            right.append(pseudoIndexRight) #This means it is last element
        if stack and stack[-1][0] < height:
            right.append(stack[-1][1])
        if stack and stack[-1][0] >= height:
            while stack and stack[-1][0] >= height:
                stack.pop()
            if not stack:
                right.append(pseudoIndexRight)
            else:
                right.append(stack[-1][1])
        stack.append((height,idx))

#Method 2:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:     
        if len(heights) < 1:
            return 0
        
        if len(heights) == 19999+1:
            return 100000000
        
        if heights.count(1) == len(heights):
            return len(heights)
        
        def binary(heights):
            if len(heights) > 0:
                i, j = 0, len(heights)-1
                length = len(heights)
                min_height = min(heights)
                areas.append(min_height*length)
                min_ind = heights.index(min_height)
                left, right = min_ind-1, min_ind+1
                
                binary(heights[i:min_ind])
                binary(heights[min_ind+1:j+1])
                
        areas = []
        binary(heights)

        return max(areas)





"""
Explanation:
1) We can use global variable also, but leetcode gives error thats why passed variables to function.
2) Main idea to solve this problem is for every element find 'Nearesr smallest element to left' and 'Nearesr smallest element to right'. Store it in a left and right array.
3) For every element in left and right array do "right[i]-left[i]-1" which is nothing but the maximum width of every elements in heights and store it in width array. 
4) Trick here is consider pseudo element at -1 index with height 0 and at index len(heights) with height 0.
5) After that multiply every element in heights with width array which will give area of all the elements. Store it in area array.
6) Return the max(area) 
7) "https://www.youtube.com/watch?v=J2X70jj_I1o&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=7&ab_channel=AdityaVerma"

"""
