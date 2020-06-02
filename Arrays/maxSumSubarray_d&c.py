"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = self.divideAndConquer(nums,0,n-1)
        return res

    def maxCrossingSum(self,nums, low, high):
        mid = (low + high)//2
        global_left =- inf 
        global_right =- inf
        sum_right =0
        sum_left =0

        for i in range(mid, low-1,-1):
            sum_left+= nums[i]
            if sum_left > global_left:
                global_left = sum_left


        for i  in range(mid+1, high+1):
            sum_right+=nums[i]
            if sum_right > global_right:
                global_right =sum_right

        return global_right+global_left
    
    
    def divideAndConquer(self,nums,low,high):
        if low == high:
            return nums[low]

        mid = (low + high)//2
        left_max_sum = self.divideAndConquer(nums,low,mid)
        right_max_sum = self.divideAndConquer(nums, mid+1,high)
        max_crossing_sum= self.maxCrossingSum(nums,low,high)

        return max(left_max_sum,right_max_sum,max_crossing_sum)
