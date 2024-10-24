class Solution:
    def dividesString(self, string: str, divisor: str) -> bool:
        if len(string) % len(divisor) == 0:
            for i in range(0, len(string), len(divisor)):
                if string[i:i+len(divisor)] != divisor:
                    return False
            return True
        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        x = ""
        for i in range(1, len(str1) + 1):
            if self.dividesString(str1, str1[:i]) and self.dividesString(str2, str1[:i]):
                x = str1[:i]
        return x
