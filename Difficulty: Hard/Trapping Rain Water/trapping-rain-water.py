
class Solution:
    def maxWater(self, arr):
        # code here
        left,right = 0,len(arr)-1
        leftM, rightM  = arr[left], arr[right]
        water = 0;
        while(left<right):
            if(leftM<rightM):
                left+=1
                leftM = max(leftM, arr[left])
                water += max(0, leftM - arr[left])
            else:
                right-=1
                rightM = max(rightM, arr[right])
                water += max(0, rightM - arr[right])
        return  water


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends