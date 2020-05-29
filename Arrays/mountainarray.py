# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

"""

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        n = MountainArray.length(mountain_arr)  
       
        if(mountain_arr.get(0) == target):
            return 0
       

        max_index = self.findingPeak(mountain_arr,0 ,n-1)
        print(max_index)
        
        
        if max_index != -1:
            if target == mountain_arr.get(max_index):
                return max_index

        res = self.bsearch(mountain_arr, target, 0 ,max_index-1)
        if res != None:
            return res
        res1 = self.descsearch(mountain_arr, target, max_index+1, n-1)
        if res1 != None:
            return res1
        else:
            return -1
            
         
        
    def findingPeak(self,mountain_arr,low, high):
        mid = (low + high) // 2
        if (mountain_arr.get(mid) > mountain_arr.get(mid+1) and 
                mountain_arr.get(mid)>mountain_arr.get(mid-1)) :
                return mid
        while low <= high:
            mid = (low + high) // 2
                        
            if (mountain_arr.get(mid+1) > mountain_arr.get(mid)):
                # return self.findingPeak(mountain_arr, mid + 1, high)
                low = mid +1

            elif mountain_arr.get(mid-1) > mountain_arr.get(mid):
                # return self.findingPeak(mountain_arr, low, mid - 1)
                high = mid-1
            else:
                return mid
        return -1
    
    
    def bsearch(self,arr, x, low, high):
        while low <= high:
            mid = (low + high) // 2
            val = arr.get(mid)
            if x == val:
                return mid 
            elif x > val:
                return self.bsearch(arr, x, mid + 1, high)

            elif x < val:
                return self.bsearch(arr, x, low, mid - 1)
    
    
    def descsearch(self,arr, x, low, high):
        while low <= high:
            mid = (low + high) // 2
            val = arr.get(mid)
            if x == val:
                return mid 
            elif x < val:
                return self.bsearch(arr, x, mid + 1, high)

            else:
                return self.bsearch(arr, x, low, mid - 1)
