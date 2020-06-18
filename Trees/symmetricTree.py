"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        tempL = []
        tempR = []
        resL = []
        resR = []
        resL = self.dfsLeft(root.left, tempL)
        resR = self.dfsRight(root.right,tempR)
        if tempL == tempR:
            return True
        else:
            return False
    
    def dfsLeft(self,root, temp):
        if root == None:
            return temp.append('')
        l = self.dfsLeft(root.left,temp)
        r = self.dfsLeft(root.right,temp)

        return temp.append(root.val)

    def dfsRight(self,root, temp):
        if root == None:
            return temp.append('')
        l = self.dfsRight(root.right,temp)
        r = self.dfsRight(root.left,temp)


"""
Explanation:
1) Catch here is we need to store null value also.
2) First I stored the left subtree in a list. Then I stored right subtree in a list. Tweak here is while storing right subtree I recursively called right child first.
3) Atlast simply compared the two list and returned the result.   
"""
