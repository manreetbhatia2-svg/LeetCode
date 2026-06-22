class Solution(object):
    def countAndSay(self,n):
        if n == 1:
            return "1"
        elif n > 1:
            return (Solution.Rle(Solution.countAndSay(self,n-1)))
        
    def Rle(string):
        string += "x"  # as last_number != x so will go into the if condition 
        start = 0
        rle = ""
        for i in range(len(string) - 1):
            if string[i] != string[i+1]:
                rle += str((string[start:i+1]).count(string[start])) + str(string[start])
                start = i+1
        return(rle)

object = Solution()
print(object.countAndSay(4))
