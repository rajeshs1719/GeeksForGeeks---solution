#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
class Solution:
    def buildTree(self, inorder, preorder):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_index = 0 
        
        def construct_tree(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            preorder_index += 1
            root = Node(root_val)
            inorder_idx = inorder_map[root_val]
            root.left = construct_tree(left, inorder_idx - 1)
            root.right = construct_tree(inorder_idx + 1, right)

            return root

        return construct_tree(0, len(inorder) - 1)
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends