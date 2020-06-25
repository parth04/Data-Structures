"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return list()
        q= []
        result =[]
        level = 1
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
                
            if level%2 == 0:
                result.append(reversed(output))
            else:
                result.append(output)
            level+=1
                
        return result     

"""
Explanation:
1)I used queue to perform Breadth First traversal.
2)Used 2 loops. Outer loop is to traverse each level and inner loop is to visit every node at particular level.
3)Cnt is used to keep track of when should we change the level. Cnt will give count of nodes at particular level. We will iterate inner loop only cnt times.(means visiting all nodes at particular level.) 
4)At the beginning maintained a variable called level. Before adding list to final result list I checked level is even number or odd and based on that append the list to result list. 

"""           
