"""
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range (n):
            for j in range(i,m):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
       
            # matrix[i].reverse()
        for item in matrix:
            item[:] = item[::-1]

"""
Explanation:

Method 1:
1) In this we use 4 swaps. For explanation see youtube video 'https://www.youtube.com/watch?v=gCciKhaK2v8&t=1735s&ab_channel=FisherCoder'

Method 2:
1)I used this in above problem. Main idea is to take transpose of the give matrix then reverse the each row. Tricky part here is to set range for inner for loop. We set from outer loop till end. 

"""
