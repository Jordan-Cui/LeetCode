class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #really ugly solution + slow + takes a lot of memory
        dict1 = {}
        dict2 = {}
        for i in word1:
            if i not in dict1:
                dict1[i] = 0
            else:
                dict1[i] += 1
        for i in word2:
            if i not in dict2:
                dict2[i] = 0
            else:
                dict2[i] += 1
        if dict1 == dict2:
            return True
        dic1 = {}
        dic2 = {}
        for i in dict1:
            if not i in dict2:
                return False
            if dict1[i] in dic1:
                dic1[dict1[i]] += 1
            else:
                dic1[dict1[i]] = 0
        for i in dict2:
            if dict2[i] in dic2:
                dic2[dict2[i]] += 1
            else:
                dic2[dict2[i]] = 0
        if dic1 == dic2:
            return True
        return False
