class Solution(object):
# creating a method which checks if its a palindrome or not 
    def isPalindrome(self, s):
        new_str = ""
        for i in s.lower():
            if i >="a" and i <= "z" or i>="0" and i <= "9":
                new_str += i
        for j in range(len(new_str)):
            if new_str[j] != new_str[len(new_str)-1-j]:
                return(False)
        return(True)

# taking string input
s = input("Enter the string ")
answer = Solution()
print(answer.isPalindrome(s))