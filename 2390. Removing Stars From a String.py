class Solution:
    def removeStars(self, s: str) -> str:
      #Attempt one (TLE)
        # sList = list(s)
        # s = ""
        # i = 1
        # while i < len(sList):
        #     if sList[i] == "*":
        #         sList.pop(i)
        #         sList.pop(i - 1)
        #         i -= 1
        #     else:
        #         i += 1
        # return(''.join(sList)) 
      
      sList = []
        for i in s:
            if i == "*":
                sList.pop()
            else:
                sList.append(i)
        return(''.join(sList))
