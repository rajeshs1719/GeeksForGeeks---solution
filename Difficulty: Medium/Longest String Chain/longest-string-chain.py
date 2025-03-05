#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        words.sort(key=len)  
        dp = {}  
        longest_chain = 1  
        
        for word in words:
            dp[word] = 1 
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]  
                if predecessor in dp: 
                    dp[word] = max(dp[word], dp[predecessor] + 1)
            longest_chain = max(longest_chain, dp[word]) 
        
        return longest_chain


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends