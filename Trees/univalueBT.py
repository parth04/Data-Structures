
"""
965
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        q = []
        val = root.val
        q.append(root)
        
        while len(q):
            front = q[0]
            if front.val != val:
                return False
            
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
                
            q.pop(0)

        return True



