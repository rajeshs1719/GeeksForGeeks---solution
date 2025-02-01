#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        i=0
        sum = 0
        for j in range(len(arr)):
            sum = sum + arr[j]
            while (sum>target) and (i<=j):
                sum = sum - arr[i]
                i+=1
            if(sum == target):
                return [i+1,j+1]

        return [-1]
            

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends