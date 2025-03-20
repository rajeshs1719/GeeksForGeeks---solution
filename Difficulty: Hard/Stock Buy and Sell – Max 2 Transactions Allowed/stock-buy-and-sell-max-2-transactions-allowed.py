class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0

        profit_left = [0] * n
        min_price = prices[0]
        
        for i in range(1, n):
            min_price = min(min_price, prices[i])  # Minimum price seen so far
            profit_left[i] = max(profit_left[i-1], prices[i] - min_price)  # Max profit if sold at i

        profit_right = [0] * n
        max_price = prices[-1]
        
        for i in range(n-2, -1, -1):
            max_price = max(max_price, prices[i])  
            profit_right[i] = max(profit_right[i+1], max_price - prices[i])  # Max profit if bought at i
        
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, profit_left[i] + profit_right[i])
        
        return max_profit


#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends