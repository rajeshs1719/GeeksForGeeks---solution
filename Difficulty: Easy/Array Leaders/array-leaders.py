class Solution:
    def leaders(self, arr):
        # code here
       Leader = []
       right_most = arr[-1]
       Leader.append(right_most)
       for i in range(len(arr)-2,-1,-1):
           if arr[i]>=right_most:
               right_most=arr[i]
               Leader.append(arr[i])
       return Leader[::-1]
        


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends