class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        for i in arr:
            if i in occurences:
                occurences[i] += 1
            else:
                occurences[i] = 1
        numOccurences = {}
        for i in occurences:
            if occurences[i] in numOccurences:
                return(False)
            else:
                numOccurences[occurences[i]] = 0
        return(True)
