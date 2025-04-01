#User function Template for python3

class Solution:
    def dfs_helper(self, node, adj, visited, result):
        visited.add(node)  
        result.append(node)  
        
        for neighbor in adj[node]: 
            if neighbor not in visited:
                self.dfs_helper(neighbor, adj, visited, result)


    def dfs(self, adj):
        visited = set()
        result = []
        self.dfs_helper(0, adj, visited, result) 
        return result

#{ 
 # Driver Code Starts
import sys
#Position this line where user code will be pasted.


def main():
    tc = int(sys.stdin.readline().strip())

    for _ in range(tc):
        V = int(sys.stdin.readline().strip())
        adj = []

        for _ in range(V):
            input_line = sys.stdin.readline().strip()
            node = list(map(int, input_line.split())) if input_line else []
            adj.append(node)

        obj = Solution()
        ans = obj.dfs(adj)
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends