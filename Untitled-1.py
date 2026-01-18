class Solution(object):
    def twoSum(self, nums, target):
        for i in nums:
            for j in range (nums.index(i) + 1 ,len(nums) ):
                if (target - i) == nums[j]:
                    return (nums.index(i),j)