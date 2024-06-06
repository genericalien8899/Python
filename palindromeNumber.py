
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string

#my solution
class Solution(object):
    def isPalindrome(self, x):
        str1 = str(x)
        counter = 0
        if len(str1)==1:
            return(True)
        else:
            for i in range(len(str1)//2):
                if str1[i] == str1[(len(str1)-1)-i]:
                    counter = counter + 1
                else:
                    return(False)
                if counter == len(str1)//2:
                    return(True)
