#maximum-active-section-with-trade=1

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ones = 0
        sections = []

        i =0
        while i <n :
            if s[i] == '0' :
                j=i
                while j<n and s[j] == s[i] : j+=1
                sections.append(j-i)
                i=j
            else :
                ones+=1
                i+=1

        if len(sections) < 2 : return ones
        best = 0
        for i in range(1,len(sections)) :
            best = max(best, sections[i] + sections[i-1])
        return ones + best

                
        