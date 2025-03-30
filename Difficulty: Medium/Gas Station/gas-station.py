class Solution:
    def startStation(self, gas, cost):
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost:  
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            if fuel < 0:  
                start = i + 1
                fuel = 0  
        return start


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends