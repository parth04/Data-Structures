"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
            if root is None:
                return 0
            q= deque()
            q.append(tuple((root,root.val)))
            digits = deque()
            while q:
                cnt = len(q)
                while cnt > 0:
                    front,digit = q.pop()
                    if front.left:
                        q.appendleft(tuple((front.left,digit * 10+front.left.val)))

                    if front.right:
                        q.appendleft(tuple((front.right,digit * 10+front.right.val)))

                    if front.left is None and front.right is None:
                        digits.appendleft(digit)

                    cnt-=1
            return sum(digits)


"""
Explanation:
1) Simple did a BSF traversal using queue.
2) At every level stored the tuple of value of node at that level and digit formed till that node.
3) Check whether node is leaf node or not and then simply add number formed till current level in another queue.
4) Return sum of all the   

"""

