class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        final_ans = ''
        result = [0]* (len(num1) + len(num2))  # as max len of 2 no.s being multiplied is sum of len of individual no.
        
        for i in range(len(num2)-1,-1,-1):
            for j in range(len(num1)-1,-1,-1):
                product = int(num2[i]) * int(num1[j])
                total = product + result[i+j+1]
                result[i+j+1] = total%10
                result[i+j] += total//10
                        
        return("".join(map(str,result)).lstrip("0"))

sol = Solution()
print(sol.multiply("2","0"))