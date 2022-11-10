class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        AAA, A
        B, BB 
        """
        aliceWins = False
        As = colors.split('B')
        Bs = colors.split('A')
        
        aliceCount, bobCount = 0, 0
        for a in As:
            if len(a) >= 3:
                aliceCount += len(a) - 2
            
        for b in Bs:
            if len(b) >= 3:
                bobCount += len(b) - 2
                    
        return aliceCount > bobCount