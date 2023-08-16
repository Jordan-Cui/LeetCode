class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s += " "
        words = []
        prev = "a"
        lastspace = -1
        for i in range(len(s)):
            if s[i] == " ":
                if prev != " ":
                    words.append(s[lastspace + 1:i])
                lastspace = i
            prev = s[i]
        length = len(words) - 1
        s = words[length]
        for i in reversed(range(length)):
            s += " " + words[i]
        return(s)
