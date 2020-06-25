"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
                
                if front.right:
                    q.append(front.right)   
                if front.left:
                    q.append(front.left)
                    
                cnt-=1
                q.pop(0)
            if output:
                result.append(output[0])
        return result
        
"""
Explanation:
1)Logic here is append the last node of every level of level order traversal to the result list.
2)I used queue to perform Breadth First traversal.
3)Used 2 loops. Outer loop is to traverse each level and inner loop is to visit every node at particular level.
4)Cnt is used to keep track of when should we change the level. Cnt will give count of nodes at particular level. We will iterate inner loop only cnt times.(means visiting all nodes at particular level.)  
 
"""
