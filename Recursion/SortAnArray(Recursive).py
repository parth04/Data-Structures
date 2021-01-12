"""
912. Sort an Array
Medium

Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: #Example [0,1,5,2]
            return nums 
        temp  = nums.pop()
        self.sortArray(nums)
        nums = self.insert(nums,temp)
        return nums
    def insert(self, nums, temp):
        if len(nums) == 0 or nums[-1] <= temp:
            nums.append(temp)
            return nums
        val = nums.pop()
        self.insert(nums,temp)
        nums.append(val)
        return nums


"""
Explanation(TLE on leetcode. But recursive approach is perfect)

1) Very beautiful explanation. Watch the video "https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6&ab_channel=AdityaVerma"

"""
