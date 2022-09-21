""" 
First, we create a group of index sequences, `locations`, for each word. 
Every time `shortest` function is called, we pick up the corresponding sequences `loc1` and `loc2`. 
Then we use two pointers, `l1` and `l2`, to calculate the shortest distance. 
In each iteration, the smaller pointer moves one step forward.

Template

# p1 & p2 from two sequences: p1-> p2->
def pointers_from_two_seq(self, seq1, seq2):
    # init pointers
    p1, p2 = 0, 0       # or seq1[0], seq2[0]
    # or other condition
    while p1 < len(seq1) and p2 < len(seq2):
        # p1 index moves when satisfy the condition
        if self.p1_condition(p1):
            p1 += 1         # or p1 = next(seq1)
        # p2 index move when satisfy the condition
        if self.p2_condition(p2):
            p2 += 1         # or p2 = next(seq2)
        # process logic before or after pointers movement
        self.process_logic(p1, p2)
"""
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict
        self.dict = defaultdict(list)
        
        for i, word in enumerate(self.words):
            self.dict[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        w1, w2 = 0, 0
        indexes1, indexes2 = self.dict[word1], self.dict[word2]
        shortest = math.inf
        while w1 < len(indexes1) and w2 < len(indexes2):
            shortest = min(shortest, abs(indexes1[w1] - indexes2[w2]))
            if indexes1[w1] < indexes2[w2]:
                w1 += 1
            else:
                w2 += 1
        return shortest        

        
        
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)