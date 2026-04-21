from typing import List

"""
[MEDIUM] MAXIMUM AREA OF ISLAND
https://neetcode.io/problems/max-area-of-island

Date: 21st Apr 2026
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

    max_area = 0

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if (r < 0 or r >= ROWS or
            c < 0 or c >= COLS or
            grid[r][c] == 0):
            return 0
        
        grid[r][c] = 0
        area = 0
        for dr, dc in directions:
            area += dfs(r + dr, c + dc) 
        return area + 1

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                area = dfs(r, c)
                max_area = max(area, max_area)
    
    return max_area

grid1 = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(maxAreaOfIsland(grid1))