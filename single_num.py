class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if i in nums[nums.index(i) + 1 :]:
                continue
            else:
                return(i)

answer = Solution()
print(answer.singleNumber([1,5,3,1,3,5,6,4,4]))