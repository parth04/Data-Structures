"""
416. Partition Equal Subset Sum
Medium

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        else:
            summ = sum(nums) // 2
            print("Summ = ", summ)
            t = [[0 for s in range(summ+1)]for n in range(len(nums)+1) ]
            for i in range(len(nums) + 1):
                for j in range(summ + 1):
                    if i == 0:
                        t[i][j] = False
                    if j == 0:
                        t[i][j] = True
            for i in range(1,len(nums) + 1):
                for j in range(summ + 1):
                    if nums[i-1] <= j:
                        t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            # for i in range(len(nums) + 1):
            #     for j in range(summ + 1):
            #         print(t[i][j], end="")
            #     print()
            return t[len(nums)][summ]

"""
Explanation:
1) Depends on Knapsack => sub set sum problem => Partition Equal Subset Sum
2) For better understanding watch videos for knapsack and sub set sum problem
3) For Partition Equal Subset Sum watch "https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=5&ab_channel=AdityaVerma"
"""
