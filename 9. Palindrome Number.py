class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y: int = 0
        x2 = x
        while True:
            y = y + (x % 10)
            x = x // 10
            if x == 0:
                break
            y = y * 10
        if y == x2:
            return True
        else:
            return False
        
            
