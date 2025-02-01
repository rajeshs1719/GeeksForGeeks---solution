class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        sum = 0
        max_sum = float('-inf')
        for i in range(len(arr)):
            sum = sum+ arr[i]
            max_sum = max(max_sum, sum)
            if sum<0:
                sum=0
        return max_sum
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends