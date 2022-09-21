class Solution:
    """
    First Try failed the test case 
    1. Attempted to try with different approach
    2. Should have fixed the code - the approach was right    
    - Lesson: 
        (1) Come up with test (edge) cases before start coding or even approach the problem
        (2) Concentrate - Always makes stupid mistake
            This time, the line 19, 20 was missing
    """
    def firstTry(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        Clarification
        - word1 != word2
        - duplcate words allowed in wordDict
        - guaranteed that word1, word2 exist in wordDict
        """
        index1, index2 = -1, -1
        minDistance = math.inf
        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                minDistance = min(minDistance, abs(index1 - index2))
        return minDistance
    
    """ Possible other approaches
    - find all distances and find min diff
    - find a, b pairs, then b, a pairs with left/right pointers, then, find min
    - Sliding Window?
    - At the end... There's no elegant solution, so, just solve bruteforce
        And, coming up with bruteforce wasn't easy for me. Needs more practice
    """
    def naive(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = math.inf
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2:
                        minDistance = min(minDistance, abs(i - j))
        
        return minDistance
            
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        return self.firstTry(wordsDict, word1, word2)