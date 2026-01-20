class Solution(object):
# creating method to check plaindrome number
    def isPalindrome(self, x):
        x = str(x)
        return x== x[::-1]


# creating object
number = int(input("Enter the number "))
palindrome = Solution()
print (palindrome.isPalindrome(number))
