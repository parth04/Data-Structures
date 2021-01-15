"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

"""
#Method-1 Recursive
def knapSack(wt, val, W, n): 
  
    # Base Case 
    if n == 0 or W == 0: 
        return 0
  
    # If weight of the nth item is 
    # less or equal to the Knapsack of capacity W, 
    # then this item can be included 
    # in the optimal solution
 
    if (wt[n-1] <= W): 	  

    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included        

	return max(val[n-1] + knapSack(wt, val, W-wt[n-1], n-1), knapSack(wt, val, W, n-1) ) 
 
    else: 
        return knapSack(W, wt, val, n-1) 
  
# end of function knapSack

#Method-2 Memoization (Bottom-up)
def knapSack(wt, val, W, n):
    t = [[-1 for x in range(W + 1)] for x in range(n + 1)]
    # Base Case
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]
    # If weight of the nth item is
    # less or equal to the Knapsack of capacity W,
    # then this item can be included
    # in the optimal solution

    if (wt[n - 1] <= W):

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included

        t[n][W] = max(val[n - 1] + knapSack(wt, val, W - wt[n - 1], n - 1), knapSack(wt, val, W, n - 1))
        return t[n][W]

    else:
        t[n][W] = knapSack(W, wt, val, n - 1)
        return t[n][W]


#Method-3 Top-Down
def knapSack(wt, val, W, n):
    t = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Base Case
    for i in range (n+1):
        for j in range(W+1):
            if i== 0 or j==0:
                t[i][j] = 0

            elif (wt[i - 1] <= j):
                t[i][j] = max(val[i - 1] + t[i - 1][j - wt[i - 1]], t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return t[n][W]
 
  
  
#Driver Code 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print (knapSack(wt, val, W, n))

"""
Explanation:
1) Method 1 - Recursive "https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3&ab_channel=AdityaVerma"
2) Method 2 - Memoization "https://www.youtube.com/watch?v=fJbIuhs24zQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=4&ab_channel=AdityaVerma"
3) Method 3 - TopDown "https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=5&ab_channel=AdityaVerma"
"""

