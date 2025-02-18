#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      
        max_heap = []
        
        for (x, y) in points:
            dist = -(x**2 + y**2)  
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, x, y))
            else:
                heapq.heappushpop(max_heap, (dist, x, y))  # Pop the farthest point
        
        return [[x, y] for (_, x, y) in max_heap]
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends