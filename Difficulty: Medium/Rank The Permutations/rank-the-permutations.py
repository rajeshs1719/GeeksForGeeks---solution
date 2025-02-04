#User function Template for python3

class Solution:
    def factorial(self,n):
        fact = 1
		for i in range(2,n+1):
		    fact *= i
		return fact
		
	def findRank(self, S):
		#Code here
		n = len(S)
		rank =  1
		fact = self.factorial(n)
		
		for i in range(n):
		    fact //=(n-i)
		    smaller_count = sum(1 for j in range(i+1,n) if S[j]<S[i])
		    
		    rank += smaller_count *  fact
		    
		return rank
		

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input().strip()
        obj = Solution()
        ans = obj.findRank(str)
        print(ans)
        print("~")

# } Driver Code Ends