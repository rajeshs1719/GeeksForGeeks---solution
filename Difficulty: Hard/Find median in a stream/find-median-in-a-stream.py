from heapq import heappush, heappop

class Solution:
    def getMedian(self, arr):
        max_heap = []
        min_heap=[]
        result = []
        
        for num in arr:
            heappush(max_heap , -num)
            if min_heap and -max_heap[0]>min_heap[0]:
                heappush(min_heap, -heappop(max_heap))
                
            if len(max_heap) > len(min_heap)+1:
                heappush(min_heap, -heappop(max_heap))
                
            elif len(min_heap)>len(max_heap):
                heappush(max_heap, -heappop(min_heap))
            
            if len(max_heap) > len(min_heap):
                result.append(float(-max_heap[0]))
            else:
                result.append((float(-max_heap[0]) + float(min_heap[0]))/2.0)
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends