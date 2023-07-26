import math
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        multiplier = pow(10, len(digits) - 1)
        for i in digits:
            total += round(int(i * multiplier), round(-math.log(multiplier, 10)))
            multiplier /= 10
        total += 1
        newdigits = []
        for i in str(total):
            newdigits.append(int(i))
        return(newdigits)
