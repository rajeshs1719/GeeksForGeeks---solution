#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,arr):
        #code here
        n = len(arr)
        stack = []
        max_area = 0
        
        for i in range(n):
            while stack and arr[i]<arr[stack[-1]]:
                height = arr[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                max_area = max(max_area , height*width)
            stack.append(i)
        while stack:
            height = arr[stack.pop()]
            width = n if not stack else n - stack[-1]-1
            max_area = max(max_area, height*width)
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