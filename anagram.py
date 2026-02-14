class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!= len(t):
            return False
        else:
            for i in set(s):
                if s.count(i) != t.count(i):
                    return False
        return True     
s_in = input ("Enter 1st string ")
t_in = input ("Enter 2nd string ")
answer = Solution()
print(answer.isAnagram(s_in,t_in))
        