class Solution:
    def isWordExist(self, mat, word):
        n, m = len(mat), len(mat[0])

        def search(i, j, index):
            if index == len(word):  # If we found the full word
                return True
            if i < 0 or i >= n or j < 0 or j >= m or mat[i][j] != word[index]:  # Out of bounds or mismatch
                return False
            
            # Store the current character and mark the cell as visited
            temp = mat[i][j]
            mat[i][j] = "#"  
            
            # Move in all 4 directions (up, down, left, right)
            found = (search(i+1, j, index+1) or  
                     search(i-1, j, index+1) or  
                     search(i, j+1, index+1) or  
                     search(i, j-1, index+1))  

            # Restore the cell (backtracking)
            mat[i][j] = temp  

            return found

        # Start DFS from every cell
        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0] and search(i, j, 0):  # Start DFS if first letter matches
                    return True
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends