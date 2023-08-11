class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for i in range(min(len(word1), len(word2))):
            merged += word1[i] + word2[i]
        i += 1
        merged += word1[i:] + word2[i:]
        return(merged)
