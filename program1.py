# program1.py

class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0
        
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Initialize island count to 0
        isle_count = 0
        
        # Iterate through every cell in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'L' and not self.visited[i][j]:
                    # If land is found and it is not visited, perform a DFS
                    self.dfs(i, j)
                    isle_count += 1  # Increment the island count for each DFS call
                    
        return isle_count
    
    # Depth-first search to mark all adjacent land as visited
    def dfs(self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols or self.grid[i][j] == 'W' or self.visited[i][j]:
            return
        
        # Mark this land cell as visited
        self.visited[i][j] = True
        
        # Explore the 4 possible directions (up, down, left, right)
        self.dfs(i - 1, j)  # Up
        self.dfs(i + 1, j)  # Down
        self.dfs(i, j - 1)  # Left
        self.dfs(i, j + 1)  # Right

