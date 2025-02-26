from typing import List
class Solution:
    def maxOfMins(self, arr: List[int]) -> List[int]:
       # code here
        n = len(arr)
        
        stack = []
        left = [-1] * n  
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        right = [n] * n  
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        max_of_mins = [0] * (n + 1)
        for i in range(n):
            window_size = right[i] - left[i] - 1
            max_of_mins[window_size] = max(max_of_mins[window_size], arr[i])
        
        for i in range(n - 1, 0, -1):
            max_of_mins[i] = max(max_of_mins[i], max_of_mins[i + 1])
        
        return max_of_mins[1:]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends