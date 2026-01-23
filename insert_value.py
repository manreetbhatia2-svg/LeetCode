class Solution:
# creating a method to insert index of the target value in nums in ascending order
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if target in nums:
                return (nums.index(target))
            else:
                if i < len(nums)-1:
                    if nums[i]<target<nums[i+1]:
                        return(i+1)
                    elif target<nums[i]:
                        return i
                else:
                    if target < nums[i]:
                        return i
                    else:
                        return i+1

# taking nums and target as input
target = int(input("Enter a target value "))
nums = list(map(int,input("Enter the values of nums with space ").split()))

# creating object for the searchInsert class
search = Solution()
print(search.searchInsert())