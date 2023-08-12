class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #find divisors of length of strings
        len1 = len(str1)
        len2 = len(str2)
        gcd = ""
        for i in range(1, min(len1, len2) + 1):
            if len1 % i == 0 and len2 % i == 0:
                #check if they divide string
                divides1 = True
                divides2 = True
                for j in range(1, len1 // i):
                    #print(str1[0: i], " ", str1[i * j: i * (j + 1)], " \n")
                    if str1[0: i] != str1[i * j: i * (j + 1)]:
                        divides1 = False
                        break
                if divides1 and str1[0: i] == str2[0: i]:
                    for j in range(1, len2 // i):
                        #print(str2[0: i], " ", str2[i * j: i * (j + 1)], " \n")
                        if str2[0: i] != str2[i * j: i * (j + 1)]:
                            divides2 = False
                            break
                    if divides1 and divides2:
                        gcd = str1[0:i]
        return(gcd)
