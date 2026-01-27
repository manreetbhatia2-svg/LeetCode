class Solution(object):
    def plusOne(self, digits):
        # converting digits to string 
        digits_str = ""
        plus1_digits = []
        for i in digits:
            digits_str = digits_str + str(i)

        # adding 1 to digits in int form and converting to list items
        plus1_digits = list(map(int,str(int(digits_str)+1)))
        
        return(plus1_digits)

# taking digits input
digits  = list(map(int,input("Enter digits with space ").split()))
answer = Solution()
print(answer.plusOne(digits))