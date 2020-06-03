"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        right = [1]*n
        output = []
        for i in range(1,n):
            left[i] = nums[i-1] * left[i-1]
        print("Left : {}".format(left))
        for i in range (n-2, -1,-1):
            right[i] = nums[i+1]*right[i+1]
        print("Right : {}".format(right))
        for i in range(n):
            output.append(left[i]*right[i])
        
        return output

"""
Explanation:
Take two array left and right. 
Start filling left array from left to right & Start filling right array from right to left.
First element of left array and last element of right array would always be 1.
left[i] would contain the product of all the numbers to the left of nums[i]  
right[i] would contain the product of all the numbers to the right of nums[i].  

"""
