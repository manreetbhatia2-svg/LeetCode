a = "a"
b = "a"
# d to p
class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            for i in range (0,len(haystack)):
                if haystack[i] == needle[0]:
                    count = 1
                    for j in range(1,len(needle)):
                        if haystack[i+j] == needle[j]:
                            count += 1
                    if count == len(needle):
                        return(i)        
        else:
            return -1


word = Solution()
print(word.strStr(a,b))