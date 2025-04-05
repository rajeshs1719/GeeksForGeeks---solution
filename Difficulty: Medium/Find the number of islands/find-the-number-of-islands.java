//{ Driver Code Starts
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tc = scanner.nextInt();
        while (tc-- > 0) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            char[][] grid = new char[n][m];

            // Read the grid input
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    grid[i][j] = scanner.next().charAt(0);
                }
            }
            Solution obj = new Solution();
            int ans = obj.countIslands(grid);
            System.out.println(ans);
            System.out.println("~");
        }
        scanner.close();
    }
}

// } Driver Code Ends


class Solution {
    private int n, m;
    
    public int countIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        
        n = grid.length;
        m = grid[0].length;
        
        boolean[][] visited = new boolean[n][m];
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                
                if (!visited[i][j] && grid[i][j] == 'L') {
                    dfs(i, j, grid, visited);
                    count++;  
                }
            }
        }
        
        return count;
    }
    
    private void dfs(int row, int col, char[][] grid, boolean[][] visited) {
        visited[row][col] = true;
        
        int[] dRow = {-1, -1, -1,  0, 0, 1, 1, 1};
        int[] dCol = {-1,  0,  1, -1, 1, -1, 0, 1};
        
        for (int i = 0; i < 8; i++) {
            int newRow = row + dRow[i];
            int newCol = col + dCol[i];
            
            if (isSafe(newRow, newCol, grid, visited)) {
                dfs(newRow, newCol, grid, visited);
            }
        }
    }
    
    private boolean isSafe(int r, int c, char[][] grid, boolean[][] visited) {
        return r >= 0 && r < n && c >= 0 && c < m && 
               grid[r][c] == 'L' && !visited[r][c];
    }
}