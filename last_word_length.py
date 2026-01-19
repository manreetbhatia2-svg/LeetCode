class Solution(object):
    #creating a method that counts the length of the last word 
    def lengthOfLastWord(self, s):
        word_len = 0
        ahead = 1
        for i in range (len(s)-1,-1,-1):
            if not(("A" <=(s[i]) <= "Z") or
                   ("a" <=(s[i]) <= "z") or 
                   ((s[i]) == (" "))):
                print ("Only english letters and spaces are allowed")
                ahead = 0
        if ahead == 1:        
            for i in range (len(s)-1,-1,-1):
                if word_len == 0 and s[i] == " ":
                    continue
                elif s[i] != " ":
                    word_len += 1
                else:
                    break
            return word_len
# creating an object which calls the method lengthOfLastWord          
word = Solution()
print(word.lengthOfLastWord("All the best "))
        