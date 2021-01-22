"""
239. Sliding Window Maximum
Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]


"""

#Method-1 Brute Force:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        if k == 1:
            return nums

        
        ans = []
        for i in range(len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
            
        print("Ans = ", ans)
        return ans

Method-2 Using Deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        if k == 1:
            return nums

        i = 0
        # j = 0
        deq = Deque()
        ans = []
        for j in range(len(nums)):
            #Calculations
            while deq and deq[-1] < nums[j]:
                deq.pop()
            deq.append(nums[j])
            # if j-i+1 < k:
            #     j+=1
            #     continue
            if j-i+1 == k:
                #ans
                ans.append(deq[0])
                #Slide the window
                if deq[0] == nums[i]:
                    deq.popleft()
                i+=1
                # j+=1
        return ans


"""
Explanaton:
1) "https://www.youtube.com/watch?v=xFJXtB5vSmM&ab_channel=AdityaVerma"
2) https://leetcode.com/problems/sliding-window-maximum/discuss/759602/Python3-Sliding-Window-O(n)-solution-using-deque-with-explanations-and-comments

"""



