class Solution:
    def maxValue(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])

        def rob_linear(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]

        return max(rob_linear(arr[:-1]), rob_linear(arr[1:]))


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends