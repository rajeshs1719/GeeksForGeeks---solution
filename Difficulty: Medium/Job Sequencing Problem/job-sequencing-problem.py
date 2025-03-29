class Solution:
    def find(self, parent, x):
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def jobSequencing(self, deadline, profit):
        jobs = sorted(zip(deadline, profit), key=lambda x: -x[1])  # Sort jobs by max profit
        max_deadline = max(deadline)

        parent = [i for i in range(max_deadline + 1)]  # Disjoint Set (Union-Find)

        total_jobs = 0
        max_profit = 0

        for d, p in jobs:
            available_slot = self.find(parent, min(d, max_deadline))  # Find latest available slot

            if available_slot > 0:
                parent[available_slot] = self.find(parent, available_slot - 1)  # Union (mark slot as filled)
                total_jobs += 1
                max_profit += p

        return [total_jobs, max_profit]
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends