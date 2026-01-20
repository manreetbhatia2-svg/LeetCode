class Solution(object):
    #creating a method that counts the length of the last word 
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])
# creating an object which calls the method lengthOfLastWord          
word = Solution()
print(word.lengthOfLastWord("All the best  "))
        