#User function Template for python3
from collections import Counter

class Solution:
    
    #Function to find the smallest window in the string s1 consisting
    #of all the characters of string s2.
    def smallestWindow(self, s1, s2):
        #code here
        if not s1 or not s2:
            return ""
        
        s2_freq = Counter(s2)
        required_chars = len(s2_freq)
        
        left = 0
        min_len = float('inf')
        min_start = 0
        formed= 0
        window_freq = {}
        
        for right, char in enumerate(s1):
            window_freq[char] = window_freq.get(char,0)+1
            
            if char in s2_freq and window_freq[char] == s2_freq[char]:
                formed += 1
            
            while formed == required_chars:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    min_start = left

                left_char = s1[left]
                window_freq[left_char] -= 1
                if left_char in s2_freq and window_freq[left_char] < s2_freq[left_char]:
                    formed -= 1
                
                left += 1  
        return s1[min_start:min_start + min_len] if min_len != float("inf") else ""
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import io
import atexit
from collections import defaultdict

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s1 = input().strip()  # Read the first string from a new line
        s2 = input().strip()  # Read the second string from the next line
        obj = Solution()
        str_res = obj.smallestWindow(s1, s2)
        if len(str_res) == 0:
            print("\"\"")
        else:
            print(str_res)
        print("~")

# } Driver Code Ends