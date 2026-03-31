class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k%2 == 0 or k%5 == 0:
            return (-1)
        elif k == 1:
            return 1
        
        else:
            rem = 0
            for i in range (1,k+1):
                rem = (rem*10 + 1)%k
                if rem == 0:
                    return i
            return -1
ans = Solution()
print(ans.smallestRepunitDivByK(15))