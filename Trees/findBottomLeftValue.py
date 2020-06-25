"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""


import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q= deque()
        q.append(root)
        res=0
        while q:
            front = q.popleft()
            res =front.val
            if front.right:
                q.append(front.right)
            if front.left:
                q.append(front.left)  
        return res

"""
Explanation:
1)Instead of using 2 while loop only single loop is used.
2)Also, instead of list deque is used. It is very efficient as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.

"""
