class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        sList = [False] * n
        for i in range(n):
            if s[i] in "aeiou":
                sList[i] = True
        count = 0
        for i in range(k):
            if sList[i]:
                count += 1
        maxVowels = count
        for i in range(k, n):
            if sList[i - k]:
                count -= 1
            if sList[i]:
                count += 1
                if count > maxVowels:
                    maxVowels = count
        return(maxVowels)
