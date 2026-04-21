from typing import List

"""
[MEDIUM] NUMBER OF ISLANDS
https://neetcode.io/problems/count-number-of-islands

Date: 20th Apr 2026
Author: Diya Ramesh

Time: O(m * n)
    - where m = len(grid) :: rows
    - where n = len(grid[0]) :: cols
Space: O(m * n)
    - where m = len(grid) :: rows
    - where n = len(grid[0]) :: cols
    - worst case if recursion call stack == size of grid (i.e. max area is whole grid)
"""

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])

    num_of_islands += 1

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            grid[r][c] == "0"):
            return 0
        
        grid[r][c] = "0"
        for dr, dc in directions:
            dfs(r + dr, c + dc) 

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                dfs(r, c)
                num_of_islands += 1
    
    return num_of_islands

grid1 = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(maxAreaOfIsland(grid1))