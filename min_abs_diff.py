class Solution:
    def minimumAbsDifference(self, arr):
      
      arr.sort()
      min_diff_check = (arr[1]-arr[0])
      final_list =[]

      for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) < min_diff_check:
                min_diff_check = (arr[i+1] - arr[i])
                final_list = [[arr[i],arr[i+1]]]

            elif (arr[i+1] - arr[i]) == min_diff_check:
                final_list.append([arr[i],arr[i+1]])

      return(final_list)
arr = [4,2,1,3]
obj = Solution()
print(obj.minimumAbsDifference(arr))
