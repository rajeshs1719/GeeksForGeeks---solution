#User function Template for python3
class Solution:
    def solveSudoku(self, mat):
        def isValid(mat, row, col, num):
            
            #check the number in the given rows
            for i in range(9):
                if mat[row][i] == num:
                    return False
                    
            #check the number in the given columns
            for j in range(9):
                if mat[j][col]==num: 
                    return False
            
            startRow, startCol = 3*(row // 3), 3*(col//3)
            for i in range(3):
                for j in range(3):
                    if mat[startRow + i][startCol +j]==num:
                        return False
            return True
            
        def solve(mat):
            for row in range(9):
                for col in range(9):
                    if mat[row][col] == 0:
                        for num in range(1,10):
                            if isValid(mat,row,col,num):
                                mat[row][col] = num
                                
                                if solve(mat):
                                    return True
                                    
                                mat[row][col] = 0
                        return False
            return True
            
        solve(mat)
        return mat
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends