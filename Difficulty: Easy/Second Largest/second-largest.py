#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        firstMax = float('-inf')
        secondMax = float('-inf')
        for num in arr:
            if (num>firstMax):
                secondMax = firstMax
                firstMax = num
            elif (num<firstMax) and (num>secondMax):
                secondMax = num
        return secondMax if secondMax != float('-inf') else -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends