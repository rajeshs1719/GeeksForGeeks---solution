class Solution:
    def equalPartition(self, arr):
        total_sum = sum(arr)
        
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        n = len(arr)
        
        dp = [False] * (target_sum + 1)
        dp[0] = True  
        for num in arr:
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target_sum]


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends