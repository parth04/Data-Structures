"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n  = len(nums)
        solution_set = [0]*n
        total = 0
        for i in range(n):
            if total < 0:
                total =0
            total += nums[i]
            solution_set[i] =total
        return max(solution_set)
        
        
