"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.buildTree(nums)
    
    def buildTree(self,nums):
        if nums == None:
            return
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums) //2
        
        root = TreeNode(nums[mid])
        root.left = self.buildTree(nums[:mid])
        
        if mid < len(nums) -1:
            root.right = self.buildTree(nums[mid+1:])
        return root        
    
        
"""
Explanation:
1)Basic idea here is, we are given with sorted array, so mid of that array we can take it as root(If array is even you can take either mid or mid+1). Sub array to the left of mid will be in left subtree and sub-array to the right of mid will be in right subtree.
2)In the recursion we first check if the sub-array is empty or not. Secondly we will check if length of subarray is 1 then create a node and return it.
3) Basic recursion works till subarray has only one element.    

"""




