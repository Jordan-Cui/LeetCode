class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return(True)
        idx = 0
        largest = len(s)
        for i in t:
            if i == s[idx]:
                idx += 1
                if idx == largest:
                    return(True)
        return(False)
