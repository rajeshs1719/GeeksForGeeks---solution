class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))
        
        dp = [[0] * n for _ in range(k + 1)]
        

        for t in range(1, k + 1):
            prev_max = -prices[0] 
            for j in range(1, n):
                dp[t][j] = max(dp[t][j-1], prices[j] + prev_max)
                prev_max = max(prev_max, dp[t-1][j] - prices[j])
        
        return dp[k][n - 1]

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends