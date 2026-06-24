'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.'''
class Solution(object):
    def multiply(self, num1, num2):
        answer = 0
        place1 = 1
        for i in num1[::-1]:
            place2 = 1
            for j in num2[::-1]:
                answer += place1 * int(i) * place2 * int(j)
                place2 = place2*10
            place1 = place1*10

    
        return str(answer)
    
sol = Solution()
print(sol.multiply('12','13'))