"""
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 
Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5

"""

#Method 1
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        stack.append(arr[-1])
        for i in range(len(arr)-2,-1,-1):
            x = arr[i]
            if not stack:
                stack.append(x)
                continue
            
            arr[i] = stack[-1]
            if stack[-1] < x:
                stack.pop()
                stack.append(x)
         
        arr [-1] = -1
        # print("arr",arr)
        return arr

#Method 2
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = 0
        maxVal = (arr[-1])
        for i in range(len(arr)-2,-1,-1):
            x = arr[i]
            
            arr[i] = maxVal
            if maxVal < x:
                maxVal = x
         
        arr [-1] = -1
        return arr


"""
Explanation:

1)For more detail explanation watch 'https://www.youtube.com/watch?v=NXOOYYwpbg4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=2&ab_channel=AdityaVerma'
2)Basic idea here is whenever there is nested for loop we can 100% times use stack to solve the problem in < O(n^2).
3)In method 1 (which is generic solution to all such problems) For every element in given array,starting from left I maintained maximum val in stack among all the elements to its right.
4)Before returning the array replaced last element with -1.

5)In method 2 (which is not generic and applicable to only this problem) instead of stack I mainatined a maxVal variable. If given element in the array is greater than maxVal then replace maxVal with that value. But before replcaing maxVal value replace arr[i] = maxVal

"""
