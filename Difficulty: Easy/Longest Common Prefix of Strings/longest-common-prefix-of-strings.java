//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String arr[] = read.readLine().trim().split(" ");

            Solution ob = new Solution();
            String ans = ob.longestCommonPrefix(arr);

            if (ans.isEmpty()) {
                System.out.print("\"\"");
            } else {
                System.out.print(ans);
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


// User function Template for Java
class Solution {
    public String longestCommonPrefix(String arr[]) {
        // code here
        if (arr == null || arr.length == 0){
            return  "";
        }
        String prefix = arr[0];
        for (int i=1;i<arr.length; i++){
            while (arr[i].indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() -1);
                if (prefix.isEmpty()){
                    return "";
                }
            }
        }
        return prefix;
    }
}