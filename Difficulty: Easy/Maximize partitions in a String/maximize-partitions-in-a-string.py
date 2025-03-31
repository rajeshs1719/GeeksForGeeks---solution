class Solution:
    def maxPartitions(self, s):
        last_occurrence = {ch: i for i, ch in enumerate(s)} 
        partitions = 0
        end = 0
        
        for i, ch in enumerate(s):
            end = max(end, last_occurrence[ch])  
            if i == end:  
                partitions += 1
        
        return partitions

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends