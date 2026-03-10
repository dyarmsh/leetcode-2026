from typing import List

"""
[MEDIUM] VALID SUDOKU
https://leetcode.com/problems/valid-sudoku

Date: 11th March 2026
Author: Diya Ramesh

Time: O(n^2)
    - where n = #rows
    - required to check all elements in the board
Space: O(n)
    - where n = #rows
    - since sets are being re-used for each iteration

Note: O(1) for time and space since it is always a 9x9 grid
"""

def isValidSudoku(board: List[List[str]]) -> bool:        
    for i, row in enumerate(board):

        row_freq, col_freq = set(), set()

        for j, cell in enumerate(row):

            # check row
            if row[j] != "." and row[j] in row_freq: # O(1) search in hash-set
                return False
            row_freq.add(cell)

            # check column
            if board[j][i] != "." and board[j][i] in col_freq:
                return False
            col_freq.add(board[j][i])
        
    # check sub-box 
    for x in range(0, 7, 3): # 0 -> 3 -> 6
        for y in range(0, 7, 3): # 0 -> 3 -> 6
            sub_box_freq = set()

            # looks at 3 rows
            for row in board[x:x+3]: # 0:3 -> 3:6 -> 6:9

                # gets sub-boxes from L-R
                for z in range(y, y+3):  # 0:3 -> 3:6 -> 6:9
                    if row[z] != "." and row[z] in sub_box_freq:
                        return False
                    sub_box_freq.add(row[z])
        
    return True