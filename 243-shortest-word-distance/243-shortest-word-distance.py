class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
   i =    _
        acab a, b
        wordq = [2]
        wordList = [a, b]
        shortest = 
        """
        wordq = deque()
        wordList = [word1, word2]
        shortest = math.inf
        for i, word in enumerate(wordsDict):
            if word in wordList:
                if len(wordq) == 2:
                    shortest = min(shortest, abs(wordq[0]-wordq[1]))
                    wordq.popleft()
                if len(wordq) == 1:
                    if wordsDict[wordq[0]] == word:
                        wordq[0] = i
                        continue
                        
                wordq.append(i)
        if len(wordq) == 2:
            shortest = min(shortest, abs(wordq[0]-wordq[1]))
        return shortest        
            
