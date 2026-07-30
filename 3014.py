#minimum-number-of-pushes-to-type-a-word-1
class Solution:
    def minimumPushes(self, word: str) -> int:
        lengthofword = int(len(word))
        leastclicks = 0
        if lengthofword < 8 :
            leastclicks = lengthofword 
        elif lengthofword > 7 and lengthofword < 16 :
            leastclicks = 8 + 2*(lengthofword % 8)
        elif lengthofword > 15 and lengthofword < 24 :
            leastclicks = 8 + (2*8) + 3*(lengthofword %8)
        else :
            leastclicks = 8 + (2*8) + (3*8) + 4*(lengthofword %8 )
        return leastclicks