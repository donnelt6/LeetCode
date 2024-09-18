#Write a function that reverses a string. The input string is given as an array of characters s.
#You must do this by modifying the input array in-place with O(1) extra memory.

#Use a two pointer ( indice ) approach

class Solution(object):
    def reverseString(self, s):
        # s is our string (List[str])
        length = len(s)
        left = 0
        right = length -1
        # our stopping condition is when left is = right, in the middle
        while left < right :
            s[left], s[right] = s[right], s[left]
            left = left + 1 # increment our LHS pointer
            right = right - 1 # decrement our RHS pointer

# Create an instance of the Solution class
solution = Solution()

# Test case 1: Reverse a string (list of characters)
test_case = ['h', 'e', 'l', 'l', 'o']
print("Original list:", test_case)

# Call the reverseString method
solution.reverseString(test_case)

# Print the result to verify if it's reversed
print("Reversed list:", test_case)