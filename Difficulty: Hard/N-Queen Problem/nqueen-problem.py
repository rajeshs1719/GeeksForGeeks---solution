#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def isSafe(board, row,col):
            for prev_col in range(col):
                prev_row  = board[prev_col]
                if prev_row == row or abs(prev_row-row)==abs(prev_col - col):
                    return False
            return True
            
        def backtrack(col, board):
            if col == n:
                solutions.append(board[:])
                return
            for row in range(1,n+1):
                if isSafe(board, row, col):
                    board[col] = row
                    backtrack(col+1, board)
                    board[col] =0
            
        solutions = []
        board = [0] * n
        backtrack(0, board)
        return solutions
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends