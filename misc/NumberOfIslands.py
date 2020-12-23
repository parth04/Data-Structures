"""
200. Number of Islands
Medium

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         noOfIcelands = 0
#         for x in range(rows):
#             for y in range(cols):
#                 if grid[x][y] == '1':
#                     noOfIcelands+=1
#                     self.dfs(grid, x , y, rows, cols )
#         return noOfIcelands
                
#     def dfs(self , grid, x, y, rows, cols):
#         if (x<0 or x>=rows or y<0 or y>=cols or grid[x][y]!='1'):
#             return
#         grid[x][y] = 'visited'
#         self.dfs(grid, x+1,  y, rows, cols) #right
#         self.dfs(grid, x-1,  y, rows, cols) #left
#         self.dfs(grid, x,  y+1, rows, cols) #top
#         self.dfs(grid, x,  y-1, rows, cols) #bottom


        rows = len(grid)
        cols = len(grid[0])
        noOfIcelands = 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == '1':
                    noOfIcelands+=1
                    self.bfs(grid, x , y,rows,cols)
        return noOfIcelands
                
    def bfs(self , grid, x, y, rows, cols):
        dqueue = collections.deque()
        dqueue.append((x,y))
        grid[x][y] = "visited"
        
        while dqueue:
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            i, j = dqueue.popleft()
            for d in directions:
                di = i + d[0]
                dj = j + d[1]
                
                if (self.isValid(grid,di,dj,rows,cols) and grid[di][dj]=="1"):
                    dqueue.append((di,dj))
                    grid[di][dj] = "visited"
    def isValid(self, grid,di,dj,rows,cols):
        if (di<0 or di>=rows or dj<0 or dj>=cols):
            return False
        return True
        
                    
"""
Explanation:
1) DFS : https://www.youtube.com/watch?v=__98uL6wst8&t=566s
2) BFS :https://www.youtube.com/watch?v=S1u806G_JuE&t=414s&ab_channel=ProgrammingTutorials

"""
