
class Solution:
    
  
    def reversalalgo(self, nums,start,end):
        while(start < end):
            temp=nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        n = len(nums)
        k%=n
        self.reversalalgo(nums,0,n-1)
        self.reversalalgo(nums,0,k-1)
        self.reversalalgo(nums, k, n-1)
        
"""
Significance of doing k%=n is to handle cases where value of k > len(arr).
Basically what happens is if you rotate array with its length it will give you the original array.
So when we take modulus, it will give us factor by which we need to move our number.
"""  

    
    
    
    
    
