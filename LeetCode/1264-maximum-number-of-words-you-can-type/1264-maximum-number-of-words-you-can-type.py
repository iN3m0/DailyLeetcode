class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = len(text.split())
        for word in text.split():
            if any(letter in word for letter in brokenLetters):
                count -=1
        return count
