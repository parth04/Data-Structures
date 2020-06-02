# 33. Search in Rotated Sorted Array
# Medium
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4 Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        bindex = self.bsearch(sorted(nums), target, 0, n-1)
        
        if bindex == None:
            return -1
        
        rotation_factor = nums.index(min(nums))
        diff = (n-1) - bindex
        
        if diff >= rotation_factor:
            return (bindex + rotation_factor)
        
        else:
            res = (rotation_factor - diff) - 1
            return res
        

    def bsearch(self,arr, x, low, high):

        while low <= high:
            mid = (low + high) // 2
            if x == arr[mid]:
                return mid

            elif x > arr[mid]:
                low = mid+1

            elif x < arr[mid]:
                high =mid-1

        return None



# Method of solving

# Sort the array and perform binary search search on it to find the index of the target element in the sorted array.
# Now find the rotation factor by which the sorted array is rotated resulting in our given array.
# The index of 0th element of the sorted array, in the given array would be the rotation factor.

#eg: [4,5,6,7,0,1,2]
# sorted -> [0,1,2,4,5,6,7]
# 0th element of sorted array = 0. Its index in the given array = 4. Hence, rotation factor is 4

# Now check whether the target element had to perform a cycle when rotation was applied i.e move across from extreme
# right to extreme left and further (cyclic rotation)

# if no, then we can simply get the resultant index by adding the rotation factor and the element's index in the sorted array.
# if yes, then we can get the resultant index from
# "rotation factor - [(length of array - 1) - (index of target element in sorted array)] - 1"


# If the difference between (length of array - 1) and (index of target element in sorted array) < rotation factor:
    # index = rotation factor - difference - 1
# else:
    # index = 0 + (index of target element in sorted array) + rotation factor
