class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        median = 0
        nums3 = nums1 + nums2
        nums3.sort()
        print(nums3)
        for i in range(0,len(nums3)+1):
            if len(nums3)%2 == 0:
                if i == (len(nums3)/2)-1:
                    print(nums3[i])
                    print(nums3[i+1])
                    median = (nums3[i] + nums3[i+1])/2 
            else:
                if i == (len(nums3)-1)/2:
                    median = nums3[i]
        return median
ans = Solution()
print(ans.findMedianSortedArrays([1,2],[3,4]))