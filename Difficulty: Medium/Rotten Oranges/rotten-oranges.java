//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();

            int mat[][] = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) mat[i][j] = sc.nextInt();
            }
            Solution obj = new Solution();
            int ans = obj.orangesRotting(mat);
            System.out.println(ans);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    static class Pair{
        int row,col,time;
        Pair(int r,int c,int t){
            this.row =r;
            this.col = c;
            this.time = t;
        }
    }
    
    public int orangesRotting(int[][] mat) {
        if(mat == null || mat.length == 0) return -1;
        int rows = mat.length, cols = mat[0].length;
        Queue<Pair> queue = new LinkedList<>();
        int freshCount = 0, time =0;
        
        for (int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(mat[i][j]== 2){
                    queue.add(new Pair(i,j,0));
                }
                else if(mat[i][j]==1){
                    freshCount++;
                }
            }
        }
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};
        
        while(!queue.isEmpty()){
            Pair curr = queue.poll();
            int r = curr.row, c=curr.col, t = curr.time;
            time = Math.max(time,t);
            for(int[] dir : directions){
                int newRow = r + dir[0], newCol = c+dir[1];
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && mat[newRow][newCol] == 1) {
                    mat[newRow][newCol] = 2;
                    freshCount--;
                    queue.add(new Pair(newRow, newCol, t+1));
            }
        }
        
    }
    return (freshCount ==0)?time : -1;
}
}