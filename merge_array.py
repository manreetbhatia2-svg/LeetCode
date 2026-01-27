class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()

        return(nums1)
    
answer = Solution() 
print(answer.merge([1,2,9,0,0],3,[4,11],2))