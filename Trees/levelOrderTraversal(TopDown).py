
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return list()
        q= []
        result =[]
        q.append(root)

        while q:
            output = []
            cnt = len(q)
            while cnt > 0:
                front = q[0]
                output.append(front.val)
                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)
                cnt-=1
                q.pop(0)
            result.append(output)
        return result    


"""
Explanation:
1)I used queue to perform Breadth First traversal.
2)Used 2 loops. Outer loop is to traverse each level and inner loop is to visit every node at particular level.
3)Cnt is used to keep track of when should we change the level. Cnt will give count of nodes at particular level. We will iterate inner loop only cnt times.(means visiting all nodes at particular level.)  

"""
