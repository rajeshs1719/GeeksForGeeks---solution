#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    max_kadane = kadane(arr)
    total_sum = sum(arr)
    min_kadane = kadane([-x for x in arr])
    
    circular_max = total_sum + min_kadane
    
    if circular_max == 0:
        return max_kadane
    return max(max_kadane, circular_max)

def kadane(arr):
    max_sum = float('-inf')
    current_max = 0
    for num in arr:
        current_max = max(num, current_max+num)
        max_sum = max(max_sum, current_max)
    return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends