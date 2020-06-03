
"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

"""





class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        output = []
        if n1 > n2:
            nums1.sort()
            nums2.sort()
            for i in range (n2):
                idx = self.bsearch(nums1, nums2[i], 0, len(nums1)-1)
                if idx == None:
                    continue
                else : 
                    nums1.pop(idx)
                    output.append(nums2[i])
            return output
        else:
            nums2.sort()
            nums1.sort()
            for i in range (n1):
                idx = self.bsearch(nums2, nums1[i], 0, len(nums2)-1)
                if idx == None:
                    continue
                else : 
                    nums2.pop(idx)
                    output.append(nums1[i])
                    
            return output
            
            
            
    def bsearch(self,arr, x, low, high):
        while low <= high:
            mid = (low + high) // 2
            if x == arr[mid]:
                return mid
            elif x > arr[mid]:
                return self.bsearch(arr, x, mid + 1, high)

            elif x < arr[mid]:
                return self.bsearch(arr, x, low, mid - 1)



"""
Explanation:
Pop the element when you found it in a larger list.
"""
