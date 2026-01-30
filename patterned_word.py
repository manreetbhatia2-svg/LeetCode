class Solution(object):
    def wordPattern(self, pattern, s):
        word = s.split()
        if len(word) != len(pattern):
            return False

        dic = {}
        used_words = set()
        for a,b in zip(pattern,word):
            if a in dic:
                if dic[a]!= b:
                    return False
            else:
                if b in used_words:
                    return False
                else:
                    dic[a] = b
                    used_words.add(b)
        return True

word = Solution()
print(word.wordPattern("abba","blue red red green"))   