class Solution(object):
    # creating a method to remove the given element 
    def removeElement(self, nums, val):
        count_of_val = 0
        for i in range(0,len(nums)):
            if val in nums:
                nums.remove(val)
                count_of_val +=0

        return (nums)

# input nums and val
nums = list(map(int, input("Enter elements of list with space in between them ").split()))
val = int(input("Enter value to be removed "))

# creating an object 
removal = Solution()
print (removal.removeElement(nums,val))
