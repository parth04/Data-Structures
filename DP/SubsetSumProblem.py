"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.

"""

def subsetSumProblem (arr,sum,t):
    #Initialization	
    for i in range(len(arr) + 1):
        for j in range(sum + 1): 
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
    for i in range(1,len(arr) + 1):
        for j in range(1,sum + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    # for i in range(len(arr) + 1):
    #     for j in range(sum + 1):
    #         print(t[i][j], end="")
    #     print()
    return t[len(arr)][sum]


arr = [3, 34, 4, 12, 5, 2]
sum = 9
arr2 = [3, 34, 4, 12, 5, 2]
sum2 = 30
t = [[False for n in range(sum+1)]for n in range(len(arr)+1) ]
print(subsetSumProblem(arr,sum,t))

"""
Explanation:
1) Very very similar to knapsack problem. For more details watch "https://www.youtube.com/watch?v=_gPcYovP7wc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=7&ab_channel=AdityaVerma"

"""
