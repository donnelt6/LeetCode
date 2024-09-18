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


# Another way of solving this in python is using string slicing
# return s[::-1]