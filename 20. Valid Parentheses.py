class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            a = s.find("()")
            b = s.find("[]")
            c = s.find("{}")
            if a > -1:
                s = s[:a] + s[a + 2:]
                continue
            elif b > -1:
                s = s[:b] + s[b + 2:]
                continue
            elif c > -1:
                s = s[:c] + s[c + 2:]
                continue
            elif s == "":
                return True
            else:
                return False
