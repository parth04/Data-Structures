"""
36. Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        square = []
        # diagonal = []
        # d1=[]
        # d2=[]
        colBoard = [[0]*rows for i in range(cols)]
        
        # print("---------Board---------")        
        # for i in range(len(board)):
        #     print(board[i])
            
       
        for row in range (rows):
            for col in range(cols):
                colBoard[col][row] = board[row][col]
 
        # print("---------colBoard---------")        
        # for i in range(len(colBoard)):
        #     print(colBoard[i])
            
        # print("---------3*3---------")
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                square.append([board[l][c] for c in range(column, column + 3) for l in range(line, line + 3)])
        # for i in range(9):
        #     print(square[i])
            
        #case1: Check row
        flag = self.helper(board)
        # print("flag val after returning from row", flag)
        # print("---------Checked rows----------")
        
        if flag == False:
            return False
        else:
            #Case2: Check col in specially created colBoard
            flag = self.helper(colBoard)
            # print("flag val after returning from col", flag)
            # print("---------Checked cols----------")
            if flag == False:
                return flag
        
        
        #case3: Check 3*3 boxes
        flag = self.helper(square)
        # print("flag val after returning from 3*3", flag)
        # print("---------Checked 3*3----------")
        return flag
        
        
        
        #Case4: Check for diagonals
        # for row in range(rows):
        #     for col in range(cols):
        #         if row == col:
        #             d1.append(board[row][col])
        #             d2.append(board[row][-(col+1)])
        # diagonal.append(d1)
        # diagonal.append(d2)
        # print("Diagonal",diagonal)
        # self.helper(diagonal)
        # for i in range(len(diagonal)):
        #     for item in diagonal[i]:
        #         if item.isnumeric() and item in diagonal[i][diagonal[i].index(item)+1:]:
        #             return False
        # print("Diagonal",diagonal)
        
    
    
    def helper(self,lists):
        flag = True
        for i in range(len(lists)):
            for item in lists[i]:
                # print("Item before if",item)
                if item.isnumeric() and item in lists[i][lists[i].index(item)+1:]:
                    # print("Item-",item)
                    flag = False
                    return flag
        return flag

"""
Explanation:

1) The main idea here is to first check all the rows, then columns and then 3*3 squares. The trickest part is to get elements of 3*3 square.
2) I made a seperate function for checking the duplicate in sublist. In the sublist I checked for the duplicate number from the range where I first found digit till end. 

"""
