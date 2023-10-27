class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = "aa"
        count = 0
        charcount = 0
        for i in chars:
            if prev != i:
                if count != 0:
                    for j in str(count + 1):
                        chars[charcount] = j
                        charcount += 1
                chars[charcount] = i
                charcount += 1
                prev = i
                count = 0
            else:
                count += 1
        if count != 0:
            for j in str(count + 1):
                chars[charcount] = j
                charcount += 1
        return(charcount)
