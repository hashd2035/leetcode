class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1, w2 = [], []
        
        shortest = math.inf 
        for i in range(len(wordsDict)):
            if word1 == wordsDict[i]:
                w1.append(i)
            if word2 == wordsDict[i]:
                w2.append(i)
                
            if w1 and w2:
                diff = abs(w1[-1] - w2[-1])    
                if not diff:
                    diffWord1, diffWord2 = math.inf, math.inf
                    if len(w1) > 1:
                        diffWord1 = w1[-1] - w1[-2]
                    if len(w2) > 1:
                        diffWord2 = w2[-1] - w2[-2]
                    shortest = min(shortest, diffWord1, diffWord2)
                else:
                    shortest = min(shortest, abs(w1[-1] - w2[-1]))
        return shortest
                
    