class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Alice (True)
            - remove A, if both adj are A
        Bod (False)
            - remove B, if both adj are B
        Alice/Bob - cannot remove from edges
        
        if a player cannot move, he/she loses
        """
        
        # This returns all the As which occur in between the Bs
        aliceScore = sum(max(len(As) - 2, 0) for As in colors.split('B'))
        
        # This returns all the Bs which occur in between the As
        bobScore = sum(max(len(Bs) - 2, 0) for Bs in colors.split('A'))
        
        return aliceScore > bobScore
            