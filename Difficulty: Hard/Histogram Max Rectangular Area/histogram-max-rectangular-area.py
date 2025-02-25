#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

from typing import List

class Solution:
    def getMaxArea(self,arr):
        n = len(arr)
        stack =[]
        
        left = [-1]*n
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
        
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = arr[i] * width
            max_area = max(max_area, area)
        
        return max_area
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends