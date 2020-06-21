"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        hl ,hr=0,0
        output = []

        hl =  self.maxHeight(root.left)
        hr =  self.maxHeight(root.right)
        
        if hl > hr:
            return hl+1
        elif hr > hl:
            return hr+1
        else:
            return hl+1
            
    
    def maxHeight(self,node):
        if node == None:
            return 0
        
        l = self.maxHeight(node.left)
        r = self.maxHeight(node.right)
        
        if l>r:
            return  1+l
        else:
            return 1+r

"""
Explanation:
1)Same approach as finding diameter of BT.
2)Calculate the height of left subtree and right subtree copare them and return the result.

"""

