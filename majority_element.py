class Solution(object):
    def majorityElement(self, nums):
        distinct = []
        for i in nums:
            if i not in distinct:
                counting = nums.count(i)
                distinct.append(i)
                if counting > len(nums)/2:
                    return i
answer = Solution()
print(answer.majorityElement([1,2,2,4]))