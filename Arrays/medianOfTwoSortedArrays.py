
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n2 = len(nums2)
        
        for i in range (n2):
            nums1.append(nums2[i])
        
        total_len = len (nums1)
        nums1.sort()
        if total_len%2 ==0:
            res = (nums1[total_len//2] + nums1[(total_len//2) - 1]) / 2
            return res
        else:
            return nums1[total_len//2]
