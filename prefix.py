class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
      len_list = []
      for i in (strs):
        len_list.append(len(i))
      min_len = (min(len_list))
      prefix = ""
      j = 0
      while j <len(strs)-1:
          prefix += " "
          for k in range(min_len):
              if strs[j][k] == strs[j+1][k]:
                  prefix += strs[j][k]
              elif strs[j][0] != strs[j+1][0]:
                  return ""
              else:
                  break
          j += 1
      if prefix != " "*(len(strs)-1):
          return(min(prefix.split()))
      elif len(strs) == 1:
          return strs[0]
      else:
        return ""
answer = Solution()
print(answer.longestCommonPrefix(["flower","flow","flight"]))
