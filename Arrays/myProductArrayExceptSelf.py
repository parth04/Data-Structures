
"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""



import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i =0
        n = len(nums)
        output = []
        for i in range (n):
            temp = nums.pop(0)
            output.append(math.prod(nums))
            #print("Product : {}".format(math.prod(nums)))
            nums.append(temp)
            #print(nums)
        return output


"""
In this approach I used math library to use prod function which will give me multiplication of all the elements in the list.
I popped always 0th element from list -> did multiplication of rest of the elemeny in list and appended it to output list -> again appnded popped element to the last of the list

"""
