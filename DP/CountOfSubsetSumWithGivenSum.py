"""
Count of subsets with sum equal to X
Difficulty Level : Medium

Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.

Examples:

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1
Output: 4

"""

def countOfsubsetSumProblem (arr,target,t):

    for i in range(len(arr) + 1):
        t[i][0] = 1

    for i in range(1, len(arr) + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i - 1][j - arr[i - 1]] + t[i - 1][j]
            else:
                t[i][j] = t[i - 1][j]
    return t[len(arr)][target]

arr = [1,1,1,1]
target = 1
arr2 = [3, 34, 4, 12, 5, 2]
target2 = 30
t = [[0 for s in range(target + 1)] for n in range(len(arr) + 1)]
print(countOfsubsetSumProblem(arr,target,t))

"""
Explanation:
1) Watch "https://www.youtube.com/watch?v=F7wqWbqYn9g&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=9&ab_channel=AdityaVerma"

"""
