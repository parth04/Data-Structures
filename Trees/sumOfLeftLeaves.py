"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""

import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        q = deque()
        add = 0
        q.append(root)

        while q:
            front = q.popleft()
            if front.left:
                q.append(front.left)
                if front.left.left == None and front.left.right == None:
                    add+=front.left.val
            if front.right:
                q.append(front.right)
        return add  
    



"""
Explanation:
1)Like normal BFS traversal but in front.left checked one extra condition whetehr it is a leaf node or not.
"""
