class Solution(object):
    # defining a method
    def twoSum(self, nums, target):
        for i in nums:
            for j in range (nums.index(i) + 1 ,len(nums) ):
                if (target - i) == nums[j]:
                    return (nums.index(i),j)
# making object to call the method inside the class 
ans = Solution()
print(ans.twoSum)