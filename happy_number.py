class Solution(object):
    def isHappy(self, n):
        add = 0
        run = 0
        num = n
        while add != 1:
            add = 0
            run += 1
            
            digits = []
            for i in str(num):
                digits.append((int(i))**2)

            for j in digits:
                add += j
            num = add
            if run == 40:
                return(False)
        return (True)
    
answer = Solution()
print(answer.isHappy(19))