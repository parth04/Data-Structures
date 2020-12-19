"""
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #Method-1 : Using counter and method of counter called most_common(). most_common(n) Return a list of           the n most common elements and their counts from the most common to the least.
        # numsCounter = Counter(nums)    
        # return numsCounter.most_common()[0][0]
        
        #Method-2
        # return max(set(nums), key=nums.count)
        
        #Method-3: Create a dictionary with key as number and value a scount of number.
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        # cntDict = {}
        # for i in nums:
        #     if i in cntDict:
        #         cntDict[i]+=1
        #         if cntDict[i] > n//2: #As soon as counter is >n//2 return the key
        #             return i
        #     else:
        #         cntDict[i] = 1
        
        #Method-4(Most efficient): In statisticks the mode is the number that occurs most often in a data set.         So basically return the mode
        return mode(nums)
        
        #Method-5
        # numsCounter = Counter(nums) 
        # return max(numsCounter.keys(), key= numsCounter.get)
