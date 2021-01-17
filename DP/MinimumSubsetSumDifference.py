"""
Partition a set into two subsets such that the difference of subset sums is minimum
Difficulty Level : Hard

Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.
Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11
"""

def findMin(arr, n):
    validS1 = []
    summ = sum(arr)
    print("Summ = ",summ)
    t = subsetSumProblem(arr,summ) #The last row of the top down matrix will give the values of summ which can be possible with all the arr element or not

    for j in range(0,(summ//2)+1): #We just iterate upto only half values because we want absolute difference
        if t[n][j] == True: #If last row of matrix contains True that means that much summ is possible with all the elements in arr
            validS1.append(j)

    diff = float("inf")
    for i in validS1:
        diff = min(diff, summ-(2*i)) #Compared the minimum difference
    return diff
def subsetSumProblem (arr,summ):
    t = [[False for n in range(summ + 1)] for n in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        for j in range(summ + 1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
    for i in range(1,len(arr) + 1):
        for j in range(1,summ + 1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    # for i in range(len(arr) + 1):
    #     for j in range(sum + 1):
    #         print(t[i][j], end="")
    #     print()
    return t



# Driver code
# arr = [3, 1, 4, 2, 2, 1]
# arr = [1,2,7]
arr = [1,6,11,5]
n = len(arr)

print("The minimum difference between 2 sets is ", findMin(arr, n))


"""
Explanation:
1) For detail explanation watch "https://www.youtube.com/watch?v=-GtpxG6l_Mc&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=10&ab_channel=AdityaVerma"

"""
