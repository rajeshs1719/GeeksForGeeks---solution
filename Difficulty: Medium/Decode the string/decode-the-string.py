
class Solution:
    def decodedString(self, s):
        num_stack = []  # Stack to store multipliers
        str_stack = []  # Stack to store substrings
        current_str = ""  # Holds the current decoded substring
        num = 0  # Holds the current number

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  
            elif char == "[":
                num_stack.append(num)  
                str_stack.append(current_str)  
                current_str = ""  
                num = 0  
            elif char == "]":
                repeat_count = num_stack.pop()  
                previous_str = str_stack.pop() 
                current_str = previous_str + (current_str * repeat_count) 
            else:
                current_str += char  
        return current_str  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends