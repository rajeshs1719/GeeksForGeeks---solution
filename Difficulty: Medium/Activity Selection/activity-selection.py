class Solution:
    def activitySelection(self, start, finish):
        activities = sorted(zip(start, finish), key=lambda x: x[1])
        count = 0
        last_finish_time = -1

        for s, f in activities:
            if s > last_finish_time:
                count += 1
                last_finish_time = f
        return count


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends