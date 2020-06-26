"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        ht = self.maxHeight(root)
        if ht == -1:
            return False
        else:
            return True
    def maxHeight(self,root):
        if root == None:
            return 0
        l= self.maxHeight(root.left)
        if l == -1:
            return -1
        r= self.maxHeight(root.right)
        if r == -1:
            return -1
        
        if abs(l-r) > 1:
            return -1
        else:
            return 1+max(l,r)
        


"""
Explanation:
1) Calculate the difference between left and right sub tree at every node. When difference is greater than 1 simply return -1.
2)Check the value if it is -1 or not after every left and right recursive call. 

"""
