class Solution:
    def reverseVowels(self, s: str) -> str:
        indices = []
        vowels = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                indices.append(i)
                vowels.append(s[i])

        newS = ""
        indices.append(-1)
        index = 0
        for i in range(len(s)):
            if i == indices[index]:
                newS += vowels.pop()
                index += 1
            else:
                newS += s[i]
        return(newS)
