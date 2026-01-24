class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # removing duplicate elements from given nums and finding no. of unique numbers in it 
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[count] = nums[i+1]
                count +=1
        
        #removing extra duplicate elements created from the end of the nums list 
        multiply = len(nums)-count
        for j in range(multiply):
            nums.pop(len(nums)-1)
        return (f"unique numbers are: {count}\nnums: {nums}")
  
# creating ibject and giving nums input
nums = [1,2,3,3,3,4,5,5,8,15,15]
answer = Solution()
print(answer.removeDuplicates(nums))