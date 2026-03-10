class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        difference = arr[1] - arr[0] 
        for i in range(2,len(arr)):
            if difference != arr[i] - arr[i-1]:
                return False
        return True
ans = Solution()
print(ans.canMakeArithmeticProgression([1,5,3]))