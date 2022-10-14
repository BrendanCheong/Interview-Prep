from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        You can either do DFS or BFS to solve this question.
        Since this is a matrix, the time complexity is O(VE) and NOT O(V+E) [only for Adj List]
        
        To solve this question, we want to go through each cell and do a BFS/DFS if its a "1". The BFS/DFS will then visit all the neighbours of that cell in the visited set. If the cell is visited it will not add to the island count, instead it will skip the cells that are market visited. That way we only count cells that are grouped together, and not count multiple cells.
        
        edge cases:
        empty grid, empty cells.
        
        BFS:
        search for the first neighbouring cells that we see. That way we are searching for neighbours in "layers". 
        
        DFS:
        search for the most recently added neighbours. That way we are go through all closest neighbours of a cell before backtracking.
        """
        if not grid or not grid[0]:
            return 0
        
        islands, visited = 0, set()
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r: int, c: int) -> None:
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) # go in the 4 directions to find neighbours
            
            # keep finding neighbours until there are no more neighbours
            while q:
                neighbour_row, neighbour_col = q.popleft()
                #! to turn this into DFS, just do a q.pop() to get most recent cell
                # go through all directions
                for direction_row, direction_col in directions:
                    search_row, search_col = neighbour_row + direction_row, neighbour_col + direction_col
                    if (search_row in range(rows) and search_col in range(cols) and grid[search_row][search_col] == "1" and (search_row, search_col) not in visited):
                        visited.add((search_row, search_col))
                        q.append((search_row, search_col))
                
        
        
        # for every cell, do BFS to find all neigbours to form an island
        # we only want to do BFS on cells that are not visited and cells that are marked as "1"
        # as those cells are new cells in which we have not visited or created island groups
        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and grid[r][c] == "1"):
                    bfs(r, c)
                    islands += 1
        
        return islands
        

# test cases
sol = Solution()
assert sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) == 1
assert sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) == 3
assert sol.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]) == 1
assert sol.numIslands([[]]) == 0
