from typing import List

"""
[MEDIUM] VALID SUDOKU
https://leetcode.com/problems/valid-sudoku

Date: 11th March 2026
Author: Diya Ramesh

Time: O(n^2)
    - where n = #rows
    - required to check all elements in the board
Space:
"""

def isValidSudoku(board: List[List[str]]) -> bool:        
    for i, row in enumerate(board):
        row_set, col_set = set(), set()

        for j, cell in enumerate(row):
            # check row
            if row[j] != "." and row[j] in row_set:
                return False
            row_set.add(cell)

            # check column
            if board[j][i] != "." and board[j][i] in col_set:
                return False
            col_set.add(board[j][i])
        
    # check sub-box 
    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            freq = set()
            for row in board[x:x+3]: 
                for z in range(y, y+3): 
                    if row[z] != "." and row[z] in freq:
                        return False
                    freq.add(row[z])
        
    return True