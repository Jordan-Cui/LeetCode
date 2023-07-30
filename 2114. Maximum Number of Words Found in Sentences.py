class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        longest = 0
        for i in sentences:
            spaces = i.count(" ")
            if spaces > longest:
                longest = spaces
        return(longest + 1)
